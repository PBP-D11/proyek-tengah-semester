
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from wishlist.forms import *
from wishlist.draft_models import *
from home.models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from wishlist.forms import *
import datetime


# Create your views here.
def show_catalog(request):
    car_form = CarForm()
    # review_form = ReviewForm()
    context = {
        "car_form": car_form,
        # "review_form": review_form,
        "username": request.user,
    }
    return render(request, 'wishlist.html', context)


def json_car(request):
    cars = Car.objects.all()
    return HttpResponse(serializers.serialize("json", cars, use_natural_foreign_keys=True, use_natural_primary_keys=True), content_type="application/json")


# def json_review(request):
#     reviews = Review.objects.all()
#     return HttpResponse(serializers.serialize("json", reviews, use_natural_foreign_keys=True, use_natural_primary_keys=True), content_type="application/json")


@csrf_exempt
def create_car(request):
    car = CarForm()
    if request.method == "POST":
        car = CarForm(request.POST)
        if car.is_valid():
            name = request.POST.get('name')
            price = request.POST.get('price')
            picture = request.POST.get('picture')
        new_car = Car.objects.create(
            name=name, price=price, total_love=0,  picture=picture)
        new_car.save()

        result = {
            'fields': {
                'name': new_car.text,
                'price': new_car.text,
                # 'is_reviewed': new_car.is_reviewed,
                'total_love': new_car.total_love,
                # 'total_review': new_car.total_review,
                'picture': new_car.picture,
            },
            'pk': new_car.pk
        }

        context = {
            'car_form': car,
            'car_data': result,
        }

        return JsonResponse(context)


# @csrf_exempt
# def create_review(request, id):
#     review = ReviewForm()
#     if request.method == "POST":
#         review = ReviewForm(request.POST)
#         if review.is_valid():
#             text = review.cleaned_data['text']
#             car = get_object_or_404(Car, id=id)
#             car.is_reviewed = True
#             car.total_review += 1
#             car.save()

#             user = get_object_or_404(CustomUser, id=request.user.id)
#             new_review = Review.objects.create(
#                 text=text, car=car, user=user, date=datetime.date.today())
#             new_review.save()
#             result = {
#                 'fields': {
#                     'text': new_review.text,
#                     'car_id': id,
#                     'date': new_review.date,
#                     'user': new_review.user.username,
#                     'total_review': car.total_review,
#                 },
#                 'pk': new_review.pk
#             }

#             return JsonResponse(result)
#     return HttpResponse(status=400)


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


# @csrf_exempt
# def delete_review(request, id):
#     if request.method == "DELETE":
#         review = get_object_or_404(review, id=id)
#         if request.user == review.user:
#             question = get_object_or_404(Car, id=review.car.pk)
#             question.total_review -= 1
#             question.save()
#             review.delete()
#             result = {
#                 'id': question.pk,
#                 'total_review': question.total_review,
#             }
#             return JsonResponse(status=202, data=result)
#     return HttpResponse(status=400)

# def show_wishlist(request):
# Create your views here.
# @login_required(login_url='/login/')
# @csrf_exempt
# def create_diary_ajax(request):
#     if request.method == 'POST':
#         form = TambahDiaryForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             description = form.cleaned_data.get('description')
#             abstract = form.cleaned_data.get('abstract')
#             emotion = form.cleaned_data.get('emotion')
#             diary = DiaryBund.objects.create(title = title, abstract = abstract, description = description, emotion = emotion, date = datetime.datetime.now(), user = request.user)
#             diary.save()
#             context = {
#                 'pk' : diary.pk,
#                 'fields' : {
#                     'title' : diary.title,
#                     'description' : diary.description,
#                     'abstract' : diary.abstract,
#                     'emotion' : diary.emotion,
#                     'date' : diary.date,
#                 }
#             }
#             return JsonResponse(context)
#         return JsonResponse({'error': True})

# @login_required(login_url='/login/')
# @csrf_exempt
# def edit_diary_ajax(request, id):
#     if request.method == 'POST':
#         form = TambahDiaryForm(request.POST)
#         if form.is_valid():
#             diaryBaru = get_object_or_404(DiaryBund, id = id)
#             diaryBaru.title = form.cleaned_data.get('title')
#             diaryBaru.description = form.cleaned_data.get('description')
#             diaryBaru.abstract = form.cleaned_data.get('abstract')
#             diaryBaru.emotion = form.cleaned_data.get('emotion')
#             diaryBaru.save()
#             context = {
#                 'pk' : diaryBaru.pk,
#                 'fields' : {
#                     'title' : diaryBaru.title,
#                     'description' : diaryBaru.description,
#                     'abstract' : diaryBaru.abstract,
#                     'emotion' : diaryBaru.emotion,
#                     'date' : diaryBaru.date,
#                 }
#             }
#             return JsonResponse(context)
#         return JsonResponse({'error': True})

# @login_required(login_url='/login/')
# @csrf_exempt
# def delete_ajax(request, id):
#     if (request.method == 'DELETE'):
#         DiaryBund.objects.filter(id=id).delete()
#         return HttpResponse(status=202)

# @login_required(login_url='/login/')
# def show_json(request):
#     data_diary = DiaryBund.objects.filter(user = request.user)
#     return HttpResponse(serializers.serialize("json", data_diary), content_type="application/json")

# @login_required(login_url='/login/')
# def show_diarybund(request):
#     modelDiary = DiaryBund.objects.filter(user = request.user)
#     user_type = request.user.groups.all()[0].name
#     form = TambahDiaryForm()
#     context = {
#         'data' : modelDiary,
#         'form': form,
#         'user_type' : user_type,
#     }
#     return render(request, 'diarybund.html', context)
