# Generated by Django 4.1.2 on 2022-10-28 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carservice',
            name='photo',
            field=models.ImageField(upload_to='images'),
        ),
    ]
