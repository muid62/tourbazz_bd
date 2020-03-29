from django.shortcuts import render
from blog.models import Package, Category, Review
from django.core.paginator import Paginator
from .choice_blog import day_item,locations_item_blog


def packages(request):
    data = Package.objects.order_by('-date')
    latest_post = Package.objects.order_by('-created_at')
    category = Category.objects.all()

    paginator = Paginator(data,3)
    pages = request.GET.get('page')
    data_pages = paginator.get_page(pages)
    context = {
        'data': data_pages,
        'category':category,
        'latest_post':latest_post,
        'days': day_item,
        'location': locations_item_blog,

    }
    return render(request,'blog/blog.html', context)

def single_blog(request,blog_id):
    data = Package.objects.filter(pk=blog_id)
    review = Review.objects.all()
    context = {
        'listings': data,
        'review' : review,
        'days': day_item,
        'location': locations_item_blog,
    }
    return render(request,'blog/single_blog.html',context)


def search_package(request):
    listing = Package.objects.order_by('-date')

    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            listing = listing.filter(location__iexact=location)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            listing = listing.filter(price__lte=price)

    if 'day' in request.GET:
        day = request.GET['day']
        if day:
            listing = listing.filter(day__startswith=day)

    context = {
        'data': listing,
        'days': day_item,
        'location': locations_item_blog,
    }
    return render(request, 'blog/package_search.html', context)