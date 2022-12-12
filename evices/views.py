import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from evices.forms import AddForm
from evices.models import CarService
# Create your views here.

def show_evices_ajax(request):
    form = AddForm()
    all_kota = set()
    all_car_service = CarService.objects.all()
    for element in all_car_service:
        all_kota.add(element.city)
    context = {
        'form' : form,
        'daftar_kota' : all_kota
    }
    return render(request, "evices.html", context)

def show_evices_filtered(request, kota):
    form = AddForm()
    all_kota = set()
    all_car_service = CarService.objects.all()
    for element in all_car_service:
        all_kota.add(element.city)
    context = {
        'form' : form,
        'kota' : kota,
        'daftar_kota' : all_kota
    }
    return render(request, "evices-filtered.html", context)

def show_evices_json(request):
    all_car_service = CarService.objects.all()
    return HttpResponse(serializers.serialize("json", all_car_service), content_type="application/json")

def show_json_filtered(request, kota):
    filtered_car_service = CarService.objects.filter(city=kota)
    return HttpResponse(serializers.serialize("json", filtered_car_service), content_type="application/json")

@csrf_exempt
def add_evices_ajax(request):
    if request.method == 'POST':
        this_car_service = CarService()
        this_car_service.name = request.POST.get('name')
        this_car_service.phone = request.POST.get('phone')
        this_car_service.address = request.POST.get('address')
        this_car_service.city = request.POST.get('city')
        this_car_service.photo = request.POST.get('photo')
        this_car_service.time_open = request.POST.get('time_open')
        this_car_service.time_close = request.POST.get('time_close')
        this_car_service.link_gmap = request.POST.get('link_gmap')
        this_car_service.save()

        return JsonResponse({"message":"SUCCESS"})
