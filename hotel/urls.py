from django.urls import path
from .views import hotels,single_hotel


urlpatterns = [
   path('hotels',hotels,name='hotels'),
   path('single_hotel/<int:hotel_id>',single_hotel,name='single_hotel'),
]
