from django import forms

class InputForm(forms.Form):
    nama_station = forms.CharField(label="Nama Station", widget=forms.TextInput(attrs={'placeholder': 'Nama Station'}))
    kota = forms.CharField(label="Kota", widget=forms.TextInput(attrs={'placeholder': 'Kota'}))
    alamat = forms.CharField(label="Alamat", widget=forms.TextInput(attrs={'placeholder': 'Alamat'}))
    time_open = forms.TimeField(label="Jam Buka", widget=forms.TimeInput(attrs={'type': 'time'}))
    time_close = forms.TimeField(label="Jam Tutup", widget=forms.TimeInput(attrs={'type': 'time'}))
    link_gmap = forms.URLField(label="Link Google Map", widget=forms.URLInput(attrs={'placeholder': 'URL'}))
    