import urllib.request
import json
from django.shortcuts import render
from news.forms import InputForm
from django.core import serializers
from news.models import News
from django.http import HttpResponse, HttpResponseNotFound

api_key = "8af64132e19d4632b4ce545473cbce40"


def news(request):
	res = urllib.request.urlopen("https://newsapi.org/v2/everything?q=electric-vehicles&pageSize=10&sortBy=popularity&apiKey="+api_key).read()
	json_data = json.loads(res)
	t_length = len(json_data["articles"])

	# Create some python lists
	author = []
	title = []
	description = []
	url = []
	image = []

	for i in range(t_length):
		author.append(json_data["articles"][i]["author"])
		title.append(json_data["articles"][i]["title"])
		description.append(json_data["articles"][i]["description"])
		url.append(json_data["articles"][i]["url"])
		image.append(json_data["articles"][i]["urlToImage"])
	zipped_data = zip(author, title, description, url, image)

	return render(request, "news.html", {"zipped": zipped_data})

def show_json(request):
    news_url = News.objects.all()
    return HttpResponse(serializers.serialize("json", news_url), content_type="application/json")

def add_news(request):
	form = InputForm()
	if request.method == "POST":
		country = InputForm(request.POST)
		newNews = urllib.request.urlopen("https://newsapi.org/v2/everything?q=electric-vehicles&country="+country+"&pageSize=10&sortBy=popularity&apiKey="+api_key).read()
		if form.is_valid():
			link_news = request.POST["link_news"]
			news = AddNews(link_news=link_news)
			news.save()
			return HttpResponse(b"CREATED", status=201)
	return render(request, "news.html", {"form": form})