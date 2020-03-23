from django.shortcuts import render
from .models import Person

def contact(request):
    if request.method=='POST':
        muid = Person(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        muid.save()

    return render(request,'contact/contact.html')

def about(request):
    return render(request,'contact/about.html')
