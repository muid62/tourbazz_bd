
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1500)

    def __str__(self):
        return self.name

