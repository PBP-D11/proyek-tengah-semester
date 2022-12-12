import json
from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from .forms import CustomUserCreationForm, UpdateUserForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.http import JsonResponse
from .models import UserProfile, CustomUser

# Create your views here.
def _redirect(request, url):
    nxt = request.GET.get("next", None)
    if nxt is not None:
        url = nxt
    return redirect(url)

def main(request):
    return render(request, 'index.html')


@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html')

@csrf_exempt
def profile_update(request):
    if request.method == 'POST':
        user = authenticate(username=request.user.username,
                            password=request.POST['password'])
        if user is None:
            return JsonResponse({"error": "Wrong password!"}, status=403)
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return JsonResponse({"message": "Your profile is updated successfully"}, status=200)
        else:
            return JsonResponse({"error": "there was an error"}, status=403)
    else:
        return HttpResponse()

def validate_username(request):
    username = request.GET.get('username')
    data = {
        'exists' : CustomUser.objects.filter(username=username).exists()
    }
    return JsonResponse(data)

def validate_email(request):
    email = request.GET.get('email')
    data = {
        'exists' : CustomUser.objects.filter(email=email).exists()
    }
    return JsonResponse(data)

def validate_phone(request):
    phone_number = request.GET.get('phone')
    data = {
        'exists' : CustomUser.objects.filter(phone_number=phone_number).exists()
    }
    return JsonResponse(data)

@login_required(login_url='/login/')
def profile_json(request):
    profile = UserProfile.objects.get(user=request.user).user
    context = {
        'full_name': profile.get_full_name(),
        'username': profile.username,
        'email': profile.email,
        'contributor': profile.is_contributor,
        'first_name': profile.first_name,
        'last_name': profile.last_name,
        'phone': profile.phone_number,
        'password': profile.password,
    }
    return JsonResponse(context)

def profile_json_flutter(request):
    if request.method == 'GET':
        user = CustomUser.objects.filter(username=request.GET.get('username'))
        profile = UserProfile.objects.get(user=user).user
        context = {
            'full_name': profile.get_full_name(),
            'username': profile.username,
            'email': profile.email,
            'contributor': profile.is_contributor,
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'phone': profile.phone_number,
            'password': profile.password,
        }
        return JsonResponse(context)

@csrf_exempt
def register_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)

        username = data["username"]
        email = data["email"]
        password1 = data["password1"]
        first_name = data["first_name"]
        last_name = data["second_name"]

        newUser = CustomUser(
        username = username, 
        email = email,
        password = password1,
        first_name = first_name,
        last_name = last_name
        )

        newUser.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    

@csrf_exempt
def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('home:main')
    context = {'form': form}
    return render(request, 'register.html', context)

@csrf_exempt
def login_user_flutter(request):
    print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return JsonResponse({
              "status": True,
              "username": request.user.username,
              "message": "Successfully Logged In!",
            }, status=200)
        else:
            return JsonResponse({
              "status": False,
              "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
          "status": False,
          "message": "Failed to Login, check your email/password."
        }, status=401)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return _redirect(request, '/')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

@csrf_exempt
def logout_user_flutter(request):
    try:
        logout(request)
        return JsonResponse({
                    "status": True,
                    "message": "Successfully Logged out!"
                }, status=200)
    except:
        return JsonResponse({
          "status": False,
          "message": "Failed to Logout"
        }, status=401)

def logout_user(request):
    logout(request)
    return _redirect(request, 'home:main')
