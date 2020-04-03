from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from .choices import state_choices, bedroom_choices, price_choices

def index(request):
    try:
        listings = Listing.objects.order_by('-list_date')[:3]
    except:
        listings = Listing.objects.order_by('-list_date')
    context = {
        'latest_listings':listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
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
