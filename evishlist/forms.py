from django import forms


class AddForm(forms.Form):
    name = forms.CharField(label="Nama ", widget=forms.TextInput(
        attrs={'placeholder': 'Nama '}))
    price = forms.CharField(label="Harga", widget=forms.TextInput(
        attrs={'placeholder': 'price'}))
    category = forms.CharField(label="Kategori", widget=forms.TextInput(
        attrs={'placeholder': 'Kategori'}))
    photo = forms.URLField(label="Photo", widget=forms.URLInput(
        attrs={'placeholder': 'URL'}))
    link_buy = forms.URLField(
        label="Link ", widget=forms.URLInput(attrs={'placeholder': 'URL'}))
