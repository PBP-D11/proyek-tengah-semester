from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Wishlist(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)])
    review = models.TextField()
    target_buy = models.DateField()
