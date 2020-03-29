from django.urls import path
from .views import hotels,single_hotel
from .views import search

urlpatterns = [
   path('hotels',hotels,name='hotels'),
   path('single_hotel/<int:hotel_id>',single_hotel,name='single_hotel'),
   path('search',search,name='search'),
]
