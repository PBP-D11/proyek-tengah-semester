# Generated by Django 4.1.2 on 2022-10-29 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChargingStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_station', models.CharField(max_length=200)),
                ('kota', models.CharField(max_length=200)),
                ('alamat', models.CharField(max_length=200)),
                ('time_open', models.TimeField(max_length=200)),
                ('time_close', models.TimeField(max_length=200)),
                ('link_gmap', models.URLField()),
            ],
        ),
    ]
