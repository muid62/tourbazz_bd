from django.shortcuts import render

def hotels(request):
    return render(request,'hotel/hotels.html')
