from django.contrib import admin

from wishlist.models import Wishlist
from django.contrib.auth.admin import UserAdmin
from home.models import CustomUser

# Register your models here.
admin.site.register(Wishlist)
