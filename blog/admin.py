from django.contrib import admin
from .models import Package,Category, Review
# Register your models here.
admin.site.register([Package, Category, Review])
