from django.db import models

# Create your models here.

class movie(models.Model):
    movie_name = models.CharField(max_length=15)
    movie_data = models.CharField(max_length=50,null=True)

class phone(models.Model):
    phone_name = models.CharField(max_length=100)
    phone_price = models.CharField(max_length=20)
    