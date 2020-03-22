from django.shortcuts import render
from blog.models import Package, Category

def packages(request):
    data = Package.objects.all()
    context = {
        'data': data
    }
    return render(request,'blog/blog.html', context)

