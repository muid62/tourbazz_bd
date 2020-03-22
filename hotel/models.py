from django.db import models
from datetime import datetime

class Location(models.Model):
    name = models.CharField(max_length=150)
    created_to = models.DateTimeField(auto_now_add=True)
    updated_to = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Room_type(models.Model):
    name = models.CharField(max_length=150)
    created_to = models.DateTimeField(auto_now_add=True)
    updated_to = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    price_details = models.TextField(blank=True)
    location = models.ForeignKey(Location,on_delete=models.DO_NOTHING)
    location_details = models.CharField(max_length=200)
    day = models.CharField(max_length=100)
    member = models.PositiveIntegerField(default=0)
    room_type = models.ForeignKey(Room_type,on_delete=models.DO_NOTHING)
    star = models.PositiveIntegerField(default=0)
    best = models.BooleanField(default=False)
    review_int = models.DecimalField(max_digits=2,decimal_places=1)
    review_str = models.CharField(max_length=50)
    main_photo = models.ImageField(upload_to='hotel/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='hotel/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='hotel/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='hotel/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='hotel/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='hotel/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='hotel/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.name









