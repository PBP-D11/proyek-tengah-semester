from dataclasses import field
from tkinter import W, Widget
from django import forms
from wishlist.models import *

# create a form


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["name", "price"]
        Widgets = {
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
            'target_buy': forms.TextInput(attrs={
                'required': True,
                'type': "text",
                'name': "price",
                'id': "price",
                'class': "form-control bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                'placeholder': "Car Price"
            }),
            ' photo': forms.URLInput(attrs={
                'required': True,
                'type': "text",
                'name': "price",
                'id': "price",
                'class': "form-control bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
                'placeholder': "Car Price"
            }),

        }
        # 'picture': forms.URLInput(attrs={
        #     'required': True,
        #     'type': "url",
        #     'name': "picture",
        #     'id': "picture",
        #     'class': "form-control bg-gray-100 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white",
        #     'placeholder': "Car Picture"
        # }),


# class ReviewForm(forms.Form):
#     class Meta:
#         model = Review
#         field = ['text']
#         Widget = {
#             'text': forms.TextInput(attrs={
#                 'class': 'form-control bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2 my-3',
#                 'type': 'text',
#                 'name': 'title',
#                 'placeholder': 'Tulis komentar...',
#                 'id': 'input-review-${data.pk}'
#             }
#             )
#         }


# class CarForm(forms.Form):
#     class Meta:
#         model = Car
#         field = ["name", "price", "image"]

#         def save(self, commit=True):
#             instance = super().save(commit=False)
#             instance.some_flag = True
#             if commit:
#                 instance.save()
#             return instance
