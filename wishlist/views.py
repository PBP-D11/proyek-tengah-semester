
from multiprocessing import context
from webbrowser import get
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from wishlist.forms import *
from wishlist.models import *
from home.models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from wishlist.forms import *
from wishlist.models import *


@csrf_exempt
def create_car_ajax(request):
    if request.method == 'POST':
        user = authenticate(username=request.user.username,
                            password=request.POST['password'])
        if user is None:
            return JsonResponse({"error": "Wrong password!"}, status=403)

        form = CarForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            price = form.cleaned_data.get('price')
            link_buy = form.cleaned_data.get('link_buy')
            photo = form.cleaned_data.get('photo')
            car = Car.objects.create(
                name=name, price=price,  user=request.user, link_buy=link_buy, photo=photo)

            car.save()
            context = {
                'pk': car.pk,
                'fields': {
                    'name': car.name,
                    'price': car.price,
                    'photo': car.photo,
                    'link_buy': link_buy,
                    'car': car
                }
            }
            return JsonResponse(context)
        return JsonResponse({'error': True})


def delete_car_ajax(request, id):
    if request.user.is_authenticated:
        if (request.method == 'DELETE'):
            Car.objects.filter(id=id).delete()
            return HttpResponse(status=202)


def show_json_car(request):
    data_car = Car.objects.all()
    return HttpResponse(serializers.serialize("json", data_car), content_type="application/json")


def show_wishlist(request):
    if request.user.is_authenticated:
        modelCar = Car.objects.filter(user=request.user)
        form = CarForm()
        context = {
            'data': modelCar,
            'form': form,
        }
        return render(request, 'wishlist.html', context)
    return render(request, 'index.html')


def show_catalog(request):
    form = CarForm()
    model_car = Car.objects.all()
    context = {
        'data': model_car,
        'form': form,
    }
    return render(request, "wishlist_catalog.html", context)


def add_catalog(request):
    if request.method == 'POST':
        this_car_Catalog = Car()
        this_car_Catalog.name = request.POST.get('name')
        this_car_Catalog.price = request.POST.get('price')
        this_car_Catalog.photo = request.POST.get('photo')
        this_car_Catalog.link_buy = request.POST.get('link_buy')
        this_car_Catalog.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()
