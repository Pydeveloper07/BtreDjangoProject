from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor

def index(request):
    # if request.method == "POST":
    #     keywords = request.POST.get('keywords')
    #     city = request.POST.get('city')
    #     state = request.POST.get('state')
    #     bedrooms = request.POST.get('bedrooms')
    #     price = request.POST.get('price')
    #     listings = Listing.objects.all().filter(city=city, state=state, bedrooms__lte=bedrooms, price__lte=price)
    #     context = {
    #         'latest_listings': listings,
    #     }
    #     return render(request, 'pages/index.html', context)

    try:
        listings = Listing.objects.order_by('-list_date')[:3]
    except:
        listings = Listing.objects.order_by('-list_date')
    context = {
        'latest_listings':listings,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    mvp_realtor = Realtor.objects.get(is_mvp=True)
    realtors = Realtor.objects.all()
    context = {
        'mvp_realtor': mvp_realtor,
        'realtors': realtors,
    }
    return render(request, 'pages/about.html', context)
