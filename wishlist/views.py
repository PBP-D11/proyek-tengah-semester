from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from wishlist.models import Wishlist
# from wishlist.forms import TambahWishlist

# Create your views here.


# @login_required(login_url='/wishlist/login/')
def show_wishlist(request):
    return render(request, "wishlist.html")
    # username = request.user.username
    wishlist_data = Task.objects.filter(user=request.user)
    context = {
        'wishlist_data': wishlist_data,
        # 'username': username,
    }
    return render(request, "wishlist.html", context)


def create_wishlist(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        rating = request.POST.get("rating")
        review = request.POST.get("review")
        new_car = Wishlist(user=request.user, name_car=name,
                           price_car=price, rating_car=rating, review_car=review)
        new_car.save()
        return HttpResponse(b"Task Created!", status=201)
    return HttpResponse("Invalid method", status_code=405)
