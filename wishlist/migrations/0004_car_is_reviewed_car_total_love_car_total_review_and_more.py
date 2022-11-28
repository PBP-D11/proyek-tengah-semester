# Generated by Django 4.1 on 2022-11-02 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wishlist', '0003_alter_car_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='is_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='car',
            name='total_love',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='car',
            name='total_review',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wishlist.car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
