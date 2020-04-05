from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from django.core.mail import send_mail
from django.contrib import messages

def inquiry(request):
    if request.method == "POST":
        if 'user_id' in request.POST:
            if request.POST['user_id']:
                user_id = request.POST['user_id']
        else:
            user_id = 0
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        realtor_email = request.POST['realtor_email']
        if request.POST['message']:
            message = request.POST['message']
        else:
            message = ""
        # Check if this inquiry has already been made
        if Contact.objects.filter(user_id=user_id, email=email, listing=listing).exists():
            messages.error(request, "You already have this inquiry!")
            return redirect('listing', listing_id)
        # Create inquiry
        inq_new = Contact.objects.create(
            listing=listing, listing_id=listing_id, name=name, email=email,
            phone=phone, message=message, user_id=user_id)
        inq_new.save()
        # Send email to realtor
        send_mail(
            'Property Listing Inquiry',
            'There has just been an inquiry for ' + listing + '. Sign in to admin page to get more info.',
            'host_email_address',
            [realtor_email, 'email_address_you_wanna_send_to'],
            fail_silently=False,
        )


        messages.success(request, "You inquiry has been made! Please wait for the response!")

        if request.user.is_authenticated:
            return redirect('dashboard')

        return redirect('listing', listing_id)