from dataclasses import field
from tkinter import W, Widget
from django import forms
from django import forms
from wishlist.models import Wishlist

# create a form


class TambahMobil(forms.ModelForm):
    class Meta:
        model = Wishlist
        field = ["name", "price", "rating", "review", "time_buy"]
        Widget = {
            'name': forms.TextInput(attrs={
                'required': True,
                'type': "text",
                'name': "name",
                'id': "name",
                'class': "bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                'placeholder': "Car Name"
            }),
            'review': forms.TextInput(attrs={
                'required': True,
                'type': "text",
                'name': "review",
                'id': "review",
                'class': "bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                'placeholder': "Car Review"
            }),
            'price': forms.TextInput(attrs={
                'required': True,
                'type': "text",
                'name': "price",
                'id': "price",
                'class': "bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                'placeholder': "Car Price"
            }),
            'rating': forms.TextInput(attrs={
                'required': True,
                'type': "text",
                'name': "rating",
                'id': "rating",
                'class': "bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                'placeholder': "Car Rating"
            }),
        }
