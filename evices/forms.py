from django import forms

class AddForm(forms.Form):
    name = forms.CharField(label="Nama Tempat Service", widget=forms.TextInput(attrs={'placeholder': 'Nama Station'}))
    phone = forms.CharField(label="Nomor Telepon", widget=forms.TextInput(attrs={'placeholder': 'phone'}))
    address = forms.CharField(label="Alamat", widget=forms.TextInput(attrs={'placeholder': 'Alamat'}))
    city = forms.CharField(label="Kota", widget=forms.TextInput(attrs={'placeholder': 'Kota'}))
    photo = forms.URLField(label="Photo", widget=forms.URLInput(attrs={'placeholder': 'URL'}))
    time_open = forms.TimeField(label="Jam Buka", widget=forms.TimeInput(attrs={'type': 'time'}))
    time_close = forms.TimeField(label="Jam Tutup", widget=forms.TimeInput(attrs={'type': 'time'}))
    link_gmap = forms.URLField(label="Link Google Map", widget=forms.URLInput(attrs={'placeholder': 'URL'}))