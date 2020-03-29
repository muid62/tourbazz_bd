from django.shortcuts import render
from hotel.models import Hotel
from hotel.choice import star_item,locations_item,room_type_item
from blog.models import Package
from blog.choice_blog import locations_item_blog,day_item

def index(request):
    listings = Hotel.objects.order_by('-list_date').filter(best=True)
    trending = Hotel.objects.all()
    packages = Package.objects.all().filter(best=True)

    context = {
        'listings': listings,
        'stars': star_item,
        'location': locations_item,
        'room_type': room_type_item,
        'trending':trending,
        'packages':packages,
        'blog_location': locations_item_blog,
        'days': day_item,
    }
    return render(request, 'home/index.html', context)


