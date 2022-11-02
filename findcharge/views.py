from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.core import serializers
from findcharge.forms import InputForm
from findcharge.models import ChargingStation
from django.contrib.auth.decorators import login_required
from history.models import History


def show_json(request):
    station = ChargingStation.objects.all()
    return HttpResponse(serializers.serialize("json", station), content_type="application/json")

def show_json_filtered(request, kota):
    station = ChargingStation.objects.filter(kota=kota)
    return HttpResponse(serializers.serialize("json", station), content_type="application/json")

def show_station(request):
    if (request.user.is_authenticated):
        user = request.user
    else:
        user = ""

    station = ChargingStation.objects.all()
    daftar_kota = set()

    for data in station:
        daftar_kota.add(data.kota)
    return render(request, "find-charge.html", {'form':InputForm(), 'daftar_kota':daftar_kota, 'user':user})

def show_filtered_station(request, kota):
    if (request.user.is_authenticated):
        user = request.user
    else:
        user = ""

    station = ChargingStation.objects.filter(kota=kota)
    all_station = ChargingStation.objects.all()
    daftar_kota = set()

    for data in all_station:
        daftar_kota.add(data.kota)
    return render(request, "find-charge-filtered.html", {'form':InputForm(), 'daftar_kota':daftar_kota, 'user':user})

def add_station(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            nama_station = data["nama_station"]
            kota = data["kota"]
            alamat = data["alamat"]
            jam_buka = data["time_open"]
            jam_tutup = data["time_close"]
            link_gmap = data["link_gmap"]

            new_station = ChargingStation(nama_station=nama_station, \
                kota=kota, alamat=alamat, time_open=jam_buka, \
                    time_close=jam_tutup, link_gmap=link_gmap)
            
            new_station.save()

            station_obj = ChargingStation.objects.filter(pk=new_station.pk)

            station_json = serializers.serialize('json', station_obj)

        return HttpResponse(station_json, content_type="application/json")

    return HttpResponseNotFound()

@login_required(login_url='/login/')
def add_history(request, pk):
    charging_station = ChargingStation.objects.get(pk=pk)
    user = request.user
    
    new_history = History(charging_station=charging_station, user=user)
    new_history.save()

    history_obj = History.objects.filter(pk=new_history.pk)
    history_json = serializers.serialize('json', history_obj)

    return HttpResponse(history_json, content_type="application/json")