from dataclasses import field
from tkinter import W, Widget
from django import forms
from django import forms
from wishlist.models import Wishlist, Car, Review

# create a form


class CarForm(forms.Form):
    class Meta:
        model = Car
        field = ["name", "price", "image"]
        Widget = {
            'name': forms.TextInput(attrs={
                'required': True,
                'type': "text",
                'name': "name",
                'id': "name",
                'class': "form-control bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                'placeholder': "Car Name"
            }),
            'price': forms.TextInput(attrs={
                'required': True,
                'type': "text",
                'name': "price",
                'id': "price",
                'class': "form-control bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                'placeholder': "Car Price"
            }),
            'picture': forms.URLInput(attrs={
                'required': True,
                'type': "url",
                'name': "picture",
                'id': "picture",
                'class': "form-control bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                'placeholder': "Car Picture"
            }),
        }


class ReviewForm(forms.Form):
    class Meta:
        model = Review
        field = ['text']
        Widget = {
            'text': forms.TextInput(attrs={
                'class': 'form-control bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2 my-3',
                'type': 'text',
                'name': 'title',
                'placeholder': 'Tulis komentar...',
                'id': 'input-review-${data.pk}'
            }
            )
        }
