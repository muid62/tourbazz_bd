from django.shortcuts import render
from .models import Hotel
from django.core.paginator import Paginator


def single_hotel(request,hotel_id):
    return render(request,'hotel/single_hotel.html')

def hotels(request):
    listings = Hotel.objects.order_by('-list_date')

    paginator = Paginator(listings,3)
    pages = request.GET.get('page')
    listings_page = paginator.get_page(pages)

    context = {
        'listings':listings_page
    }
    return render(request,'hotel/hotels.html',context)