from django.db import models
from home.models import CustomUser


class Car(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.TextField()
    price = models.TextField()
    # target_buy = models.TextField()
    # photo = models.URLField()
    # link_buy = models.URLField(max_length=200)
