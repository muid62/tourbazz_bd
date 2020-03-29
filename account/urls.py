from django.urls import path
from .views import register,login,profile,logout


urlpatterns = [
   path('account/register',register,name='register'),
   path('account/login',login,name='login'),
   path('account/profile',profile,name='profile'),
   path('account/logout',logout,name="logout"),
]
