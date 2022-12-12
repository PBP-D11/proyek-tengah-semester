import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from evishlist.forms import AddForm
from evishlist.models import Car
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def show_evishlist_ajax(request):
    form = AddForm()
    all_kategori = set()
    all_car = Car.objects.all()
    for element in all_car:
        all_kategori.add(element.category)
    context = {
        'form': form,
        'daftar_kategori': all_kategori
    }
    return render(request, "evishlist.html", context)


def show_evishlist_json(request):
    all_car = Car.objects.all()
    return HttpResponse(serializers.serialize("json", all_car), content_type="application/json")


def show_json_filtered(request, kategori):
    filtered_car = Car.objects.filter(category=kategori)
    return HttpResponse(serializers.serialize("json", filtered_car), content_type="application/json")


def add_evishlist_ajax(request):
    if request.method == 'POST':
        this_car = Car()
        this_car.name = request.POST.get('name')
        this_car.price = request.POST.get('price')
        this_car.category = request.POST.get('category')
        this_car.photo = request.POST.get('photo')
        this_car.link_buy = request.POST.get('link_buy')
        this_car.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


@csrf_exempt
def add_evishlist_flutter(request):
    if request.method == 'POST':
        data = request.POST
        name = data["name"]
        category = data["category"]
        price = data["price"]
        photo = data["photo"]
        link_buy = data["link_buy"]
        new_evishlist = Car(name=name,
                            category=category, price=price, photo=photo, link_buy=link_buy)

        new_evishlist.save()

    return JsonResponse({"message": "Berhasil!"})
