from email.policy import default
from django.db import models

from findcharge.models import ChargingStation
from home.models import CustomUser
from django.utils.timezone import now

# Create your models here.
class History(models.Model):
    date = models.DateField(default=now)
    charging_station = models.ForeignKey(ChargingStation, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)