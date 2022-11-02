from django.db import models

# Create your models here.
class CarService(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=20)
    photo = models.URLField()
    time_open = models.TimeField(max_length=200,null=True, blank=True)
    time_close = models.TimeField(max_length=200,null=True, blank=True)
    link_gmap = models.URLField(max_length=200)