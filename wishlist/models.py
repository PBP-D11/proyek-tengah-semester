from django.db import models
from home.models import CustomUser
# Create your models here.


class Car(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    is_reviewed = models.BooleanField(default=False)
    total_love = models.IntegerField(default=0)
    total_review = models.IntegerField(default=0)
    image = models.URLField()


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)


class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    # time_buy = models.DateField()
