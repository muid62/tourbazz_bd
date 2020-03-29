"""tourbazz_bd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('home/', include('home.urls'))
"""

from django.urls import path
from.views import packages
from .views import single_blog,search_package

urlpatterns = [
    path('packages',packages,name="packages"),
    path('single_blog/<int:blog_id>',single_blog,name="single_blog"),
    path('package_search',search_package,name='package_search')
]
