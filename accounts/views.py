from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('dashboard')
        else:
            messages.error(request, "Wrong credentials!")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_con = request.POST['password_con']

        if password == password_con:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is not available!")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "This email is already in use!")
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username, email=email, password=password, 
                        first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, "You've been registered successfully!")
                    return redirect('login')
        else:
            messages.error(request, "Passwords don't match!")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    inquiry_list = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': inquiry_list,
    }
    return render(request, 'accounts/dashboard.html', context)

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now logged out!")
        return redirect('index')
