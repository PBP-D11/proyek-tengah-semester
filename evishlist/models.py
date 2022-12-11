from django.db import models

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=15)
    category = models.CharField(max_length=15)
    photo = models.URLField()
    link_buy = models.URLField(max_length=200)
