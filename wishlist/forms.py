# from dataclasses import field
# from tkinter import W, Widget
from django import forms
from wishlist.models import *

# create a form


class CarForm(forms.Form):
    name = forms.CharField(label="Nama Mobil", widget=forms.TextInput(
        attrs={'placeholder': 'Nama Mobil'}))
    price = forms.CharField(label="Harga Mobil", widget=forms.TextInput(
        attrs={'placeholder': 'Harga Mobil'}))
    photo = forms.URLField(label="Photo", widget=forms.URLInput(
        attrs={'placeholder': 'URL'}))
    link_buy = forms.URLField(label="Link Membeli Mobil",
                              widget=forms.URLInput(attrs={'placeholder': 'URL'}))
