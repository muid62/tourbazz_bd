from django.contrib import admin
from .models import Location,Room_type,Hotel

class MyAdminSite(admin.AdminSite):
    admin.AdminSite.site_header = 'TourBazz Admin Panel'
    admin.AdminSite.index_title = 'TourBazz AdminSite'


class HotelAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'day', 'member', 'room_type', 'star', 'best')
    list_display_links = ('id','name',)
    list_per_page = 25


admin.site.register(Hotel,HotelAdmin)
admin.site.register(Location)
admin.site.register(Room_type)
