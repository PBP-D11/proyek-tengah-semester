from django import forms
from news.models import LinkNews, News

class InputForm(forms.ModelForm):
    url = forms.URLField(label="Link News", widget=forms.URLInput(attrs={'placeholder': 'URL'}))
    class Meta:
        model = LinkNews
        fields = ['url']

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['author', 'title', 'description', 'url', 'image']