from django import forms
from news.models import LinkNews, News

class InputForm(forms.Form):
    link_news = forms.URLField(label="Link News", widget=forms.URLInput(attrs={'placeholder': 'URL'}))
    class Meta:
        model = LinkNews
        fields = ['link_news']

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['link_news']