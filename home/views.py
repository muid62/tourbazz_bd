from django.shortcuts import render
from hotel.models import Hotel

def index(request):
    listings = Hotel.objects.order_by('-list_date').filter(best=True)
    context = {
        'listings': listings
    }
    return render(request, 'home/index.html', context)


