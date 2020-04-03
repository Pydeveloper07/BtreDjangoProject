from django.shortcuts import render, get_object_or_404
from .models import Listing
from realtors.models import Realtor
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pages.choices import state_choices, bedroom_choices, price_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {
        'listings': page_listings,
    }
    

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    mvp_realtor = get_object_or_404(Realtor, is_mvp=True)
    context = {
        'listing': listing,
        'mvp_realtor': mvp_realtor,
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_listings = Listing.objects.all()
    keywords = city = state = ''
    bedrooms = price = 0
    #Filtering by keywords
    if 'keywords' in request.POST:
        if request.POST['keywords']:
            keywords = request.POST['keywords']
            queryset_listings = queryset_listings.filter(description__icontains=keywords)

    #Filtering by city name
    if 'city' in request.POST:
        if request.POST['city']:
            city = request.POST['city']
            queryset_listings = queryset_listings.filter(city__iexact=city)

    #Filtering by state
    if 'state' in request.POST:
        if request.POST['state']:
            state = request.POST['state']
            queryset_listings = queryset_listings.filter(state__iexact=state)
    
    #Filtering by bedrooms
    if 'bedrooms' in request.POST:
        if request.POST['bedrooms']:
            bedrooms = request.POST['bedrooms']
            queryset_listings = queryset_listings.filter(bedrooms=bedrooms)

    #Filtering by price
    if 'price' in request.POST:
        if request.POST['price']:
            price = request.POST['price']
            queryset_listings = queryset_listings.filter(price__lte=price)
    
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_listings,
        'keywords': keywords,
        'city': city,
        'state': state,
        'bedrooms': bedrooms,
        'price': price,

    }
    return render(request, 'listings/search.html', context)
