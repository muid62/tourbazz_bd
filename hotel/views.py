from django.shortcuts import render
from .models import Hotel
from django.core.paginator import Paginator
from .choice import star_item,locations_item,room_type_item
from blog.choice_blog import day_item,locations_item_blog



def single_hotel(request,hotel_id):
    listings = Hotel.objects.filter(pk=hotel_id)
    context = {
        'listings':listings,
        'stars': star_item,
        'location': locations_item,
        'room_type': room_type_item,
    }
    return render(request,'hotel/single_hotel.html',context)




def hotels(request):
    listings = Hotel.objects.order_by('-list_date')

    paginator = Paginator(listings,3)
    pages = request.GET.get('page')
    listings_page = paginator.get_page(pages)

    context = {
        'listings':listings_page,
        'stars':star_item,
        'location':locations_item,
        'room_type':room_type_item,
        'blog_location': locations_item_blog,
        'days': day_item,
    }
    return render(request,'hotel/hotels.html',context)




def search(request):
    listing = Hotel.objects.order_by('-list_date')
    
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            listing = listing.filter(price__lte=price)

    if 'star' in request.GET:
        star = request.GET['star']
        if star:
            listing = listing.filter(star__exact=star)

    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            listing = listing.filter(location__name__iexact=location)

    if 'reviews' in request.GET:
        reviews = request.GET['reviews']
        if reviews:
            listing = listing.filter(review_int__startswith=reviews)


    if 'room_type' in request.GET:
        room_type = request.GET['room_type']
        if room_type:
            listing = listing.filter(room_type__name__exact=room_type)




    if 'pet' in request.GET:
        pet = request.GET['pet']
        if pet:
            listing = listing.filter(description__icontains=pet)

    if 'Car' in request.GET:
        Car = request.GET['Car']
        if Car:
            listing = listing.filter(description__icontains=Car)

    if 'Wireless' in request.GET:
        Wireless = request.GET['Wireless']
        if Wireless:
            listing = listing.filter(description__icontains=Wireless)

    if 'Reservations' in request.GET:
        Reservations = request.GET['Reservations']
        if Reservations:
            listing = listing.filter(description__icontains=Reservations)

    if 'Parking' in request.GET:
        Parking = request.GET['Parking']
        if Parking:
            listing = listing.filter(description__icontains=Parking)

    if 'Smoking' in request.GET:
        Smoking = request.GET['Smoking']
        if Smoking:
            listing = listing.filter(description__icontains=Smoking)

    if 'Wheelchair' in request.GET:
        Wheelchair = request.GET['Wheelchair']
        if Wheelchair:
            listing = listing.filter(description__icontains=Wheelchair)

    if 'Pool' in request.GET:
        Pool = request.GET['Pool']
        if Pool:
            listing = listing.filter(description__icontains=Pool)


    context = {
        'listings': listing,
        'stars': star_item,
        'location': locations_item,
        'room_type': room_type_item,
    }
    return render(request,'hotel/search.html',context)