from email.mime import image
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from wishlist.forms import CarForm, ReviewForm
from wishlist.models import Review, Wishlist, Car
from home.models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from wishlist.forms import *
import datetime


# Create your views here.
def show_car(request):
    car_form = CarForm()
    review_form = ReviewForm()
    context = {
        "car_form": car_form,
        "review_form": review_form,
        "username": request.user,
    }
    return render(request, 'wishlist.html', context)


def json_car(request):
    cars = Car.objects.all()
    return HttpResponse(serializers.serialize("json", cars, use_natural_foreign_keys=True, use_natural_primary_keys=True), content_type="application/json")


def json_review(request):
    reviews = Review.objects.all()
    return HttpResponse(serializers.serialize("json", reviews, use_natural_foreign_keys=True, use_natural_primary_keys=True), content_type="application/json")


@csrf_exempt
def create_car(request):
    car = CarForm()
    if request.method == "POST":
        car = CarForm(request.POST)
        if car.is_valid():
            name = car.cleaned_data['name']
            price = car.cleaned_data['price']
            image = car.cleaned_data['picture']
        new_car = Review.objects.create(
            name=name, price=price, is_reviewed=False, total_love=0, total_review=0, image=image)
        new_car.save()
        result = {
            'fields': {
                'name': new_car.text,
                'price': new_car.text,
                'is_reviewed': new_car.is_reviewed,
                'total_love': new_car.total_love,
                'total_review': new_car.total_review,
                'picture': new_car.picture,
            },
            'pk': new_car.pk
        }
        return JsonResponse(result)


@csrf_exempt
def create_review(request, id):
    review = ReviewForm()
    if request.method == "POST":
        review = ReviewForm(request.POST)
        if review.is_valid():
            text = review.cleaned_data['text']
            car = get_object_or_404(Car, id=id)
            car.is_reviewed = True
            car.total_review += 1
            car.save()

            user = get_object_or_404(CustomUser, id=request.user.id)
            new_review = Review.objects.create(
                text=text, car=car, user=user, date=datetime.date.today())
            new_review.save()
            result = {
                'fields': {
                    'text': new_review.text,
                    'car_id': id,
                    'date': new_review.date,
                    'user': new_review.user.username,
                    'total_review': car.total_review,
                },
                'pk': new_review.pk
            }

            return JsonResponse(result)
    return HttpResponse(status=400)


@csrf_exempt
def love_car(request, id):
    if request.method == "PATCH":
        car = get_object_or_404(car, id=id)
        car.total_love += 1
        car.save()

    result = {
        'total_love': car.total_love,
    }

    return JsonResponse(result)


@csrf_exempt
def delete_car(request, id):
    if request.method == "DELETE":
        car = get_object_or_404(car, id=id)
        car.delete()
        return HttpResponse(status=202)
    return HttpResponse(status=400)


@csrf_exempt
def delete_review(request, id):
    if request.method == "DELETE":
        review = get_object_or_404(review, id=id)
        if request.user == review.user:
            question = get_object_or_404(Car, id=review.car.pk)
            question.total_review -= 1
            question.save()
            review.delete()
            result = {
                'id': question.pk,
                'total_review': question.total_review,
            }
            return JsonResponse(status=202, data=result)
    return HttpResponse(status=400)

# def show_wishlist(request):
