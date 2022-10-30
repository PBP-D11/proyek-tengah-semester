from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.core import serializers
from findcharge.forms import InputForm
from findcharge.models import ChargingStation

def show_json(request):
    station = ChargingStation.objects.all()
    return HttpResponse(serializers.serialize("json", station), content_type="application/json")

def show_json_filtered(request, kota):
    station = ChargingStation.objects.filter(kota=kota)
    return HttpResponse(serializers.serialize("json", station), content_type="application/json")

def show_station(request):
    station = ChargingStation.objects.all()
    daftar_kota = set()

    for data in station:
        daftar_kota.add(data.kota)
    return render(request, "find-charge.html", {'form':InputForm(), 'daftar_kota':daftar_kota})

def show_filtered_station(request, kota):
    station = ChargingStation.objects.filter(kota=kota)
    all_station = ChargingStation.objects.all()
    daftar_kota = set()

    for data in all_station:
        daftar_kota.add(data.kota)
    return render(request, "find-charge-filtered.html", {'form':InputForm(), 'daftar_kota':daftar_kota})

def add_station(request):
    form = InputForm()
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            nama_station = request.POST["nama_station"]
            kota = request.POST["kota"].capitalize()
            alamat = request.POST["alamat"]
            time_open = request.POST["time_open"]
            time_close = request.POST["time_close"]
            link_gmap = request.POST["link_gmap"]
            station = ChargingStation(
                nama_station=nama_station,
                kota=kota,
                alamat=alamat,
                time_open=time_open,
                time_close=time_close,
                link_gmap=link_gmap,
            )
            station.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

