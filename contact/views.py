from django.shortcuts import render

def contact(request):
    return render(request,'contact/contact.html')

def about(request):
    return render(request,'contact/about.html')
