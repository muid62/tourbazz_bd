from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):

    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Package(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    From = models.CharField(max_length=120)
    to = models.CharField(max_length=120)
    price = models.IntegerField(default=0)
    price_details = models.TextField(blank=True)
    location = models.TextField()
    day = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    star = models.PositiveIntegerField(default=0)
    main_photo = models.ImageField(upload_to='static/images')
    photo_1 = models.ImageField(upload_to='static/images', blank=True)
    photo_2 = models.ImageField(upload_to='static/images', blank=True)
    photo_3 = models.ImageField(upload_to='static/images', blank=True)
    photo_4 = models.ImageField(upload_to='static/images', blank=True)
    photo_5 = models.ImageField(upload_to='static/images', blank=True)
    photo_6 = models.ImageField(upload_to='static/images', blank=True)

    def __str__(self):
        return self.name