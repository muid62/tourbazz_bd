from django.shortcuts import render
from .models import Hotel

def hotels(request):
    listings = Hotel.objects.all()
    context = {
        'listings':listings
    }
    return render(request,'hotel/hotels.html',context)

def single_hotel(request,hotel_id):
    return render(request,'hotel/single_hotel.html')
