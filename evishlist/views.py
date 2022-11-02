# import datetime
# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseNotFound
# from django.core import serializers
# from django.shortcuts import redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.utils import timezone
# from django.http import HttpResponseRedirect, JsonResponse
# from django.urls import reverse
# from evishlist.forms import AddForm
# from evishlist.models import CarCatalog
# # Create your views here.


# def show_evishlist_ajax(request):
#     form = AddForm()
#     all_car_Catalog = CarCatalog.objects.all()
#     context = {
#         'form': form,
#         'daftar_mobil': all_car_Catalog
#     }
#     return render(request, "evishlist.html", context)


# def show_evishlist_json(request):
#     all_car_Catalog = CarCatalog.objects.all()
#     return HttpResponse(serializers.serialize("json", all_car_Catalog), content_type="application/json")


# def add_evishlist_ajax(request):
#     if request.method == 'POST':
#         this_car_Catalog = CarCatalog()
#         this_car_Catalog.name = request.POST.get('name')
#         this_car_Catalog.price = request.POST.get('price')
#         this_car_Catalog.photo = request.POST.get('photo')
#         this_car_Catalog.link_buy = request.POST.get('link_buy')
#         this_car_Catalog.save()
#         return HttpResponse(b"CREATED", status=201)
#     return HttpResponseNotFound()
