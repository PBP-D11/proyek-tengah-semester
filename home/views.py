from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from .forms import CustomUserCreationForm,UpdateUserForm
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
        user = authenticate(username=request.user.username, password=request.POST['password'])
        if user is None:
            return JsonResponse({"error" : "Wrong password!"}, status=403)
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return JsonResponse({"message":"Your profile is updated successfully"}, status=200)
        else:
            return JsonResponse({"error": "there was an error"}, status=403)
    else:
        return HttpResponse()

def validate_username(request):
    username = request.GET.get('username',None)
    data = {
        'exists' : CustomUser.objects.filter(username=username).exists()
    }
    return JsonResponse(data)

def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'exists' : CustomUser.objects.filter(email=email).exists()
    }
    return JsonResponse(data)

def validate_phone(request):
    phone_number = request.GET.get('phone', None)
    data = {
        'exists' : CustomUser.objects.filter(phone_number=phone_number).exists()
    }
    return JsonResponse(data)

@login_required(login_url='/login/')
def profile_json(request):
    profile = UserProfile.objects.get(user=request.user).user
    context = {
        'full_name' : profile.get_full_name(),
        'username' : profile.username,
        'email' : profile.email,
        'contributor' : profile.is_contributor,
        'first_name' : profile.first_name,
        'last_name' : profile.last_name,
        'phone' : profile.phone_number,
        'password' : profile.password,
    }
    return JsonResponse(context)

def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('home:main')
    context = {'form':form}
    return render(request, 'register.html', context)

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

def logout_user(request):
    logout(request)
    return _redirect(request, 'home:main')
