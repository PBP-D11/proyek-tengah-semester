# Generated by Django 4.1.2 on 2022-11-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_remove_car_image_remove_car_is_reviewed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.TextField(),
        ),
    ]
