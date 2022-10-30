from django.db import models

# Create your models here.
class ChargingStation(models.Model):
    nama_station = models.CharField(max_length=200)
    kota = models.CharField(max_length=200)
    alamat = models.CharField(max_length=200)
    time_open = models.TimeField(max_length=200)
    time_close = models.TimeField(max_length=200)
    link_gmap = models.URLField(max_length=200)
    

