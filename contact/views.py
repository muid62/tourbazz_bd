from django.shortcuts import render
from .models import Person
from django.contrib import messages

def contact(request):
    if request.method=='POST':
        muid = Person(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        muid.save()
        messages.success(request,'Your message successfully send')
    return render(request,'contact/contact.html')

def about(request):
    return render(request,'contact/about.html')
