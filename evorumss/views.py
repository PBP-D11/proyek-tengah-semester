# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from home.models import CustomUser
from .models import Topic, Post, Comment
from .forms import CreateCommentForm

# Topic views
# def get_all_forum(request):
#     forums = Post.objects.all()
#     return HttpResponse(serializers.serialize("json", forums ), content_type="application/json")

# def get_all_forum_by_topic(request, topic):
#     forums = Post.objects.filter(topic=topic.lower())
#     return HttpResponse(serializers.serialize("json", forums ), content_type="application/json")

# def get_comment(request, forum_id):
#     if request.method == "GET":
#         forum = Post.objects.filter(id=forum_id).first()
#         comments = Comment.objects.filter(forum=forum)

#         return HttpResponse(serializers.serialize("json", comments), content_type="application/json")

def show_json_post(request):
    data = Post.objects.all()        
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def show_json_post_by_topic(request, topic):
    forumtopic = request.topic
    data = Post.objects.filter(topic = forumtopic)
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def show_json_comment(request):
    data = Comment.objects.all()        
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def show_json_topic(request):
    data = Topic.objects.all()        
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def get_comment(request, post_id):
    if request.method == "GET":
        post = Post.objects.filter(id=post_id).first()
        comments = Comment.objects.filter(post=post)

        return HttpResponse(serializers.serialize("json", comments), content_type="application/json")

@csrf_exempt
def add_comment(request, post_id):
    if request.method == "POST":
        #TODO: validate request payload
        user = CustomUser.objects.get(username=request.POST["user"])
        newComment = Comment()
        newComment.post = Post.objects.get(id=post_id)
        newComment.body = request.POST["body"]
        newComment.author = user
        newComment.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def add_post(request, topic_id):
    if request.method == "POST":
        #TODO: validate request payload
        user = CustomUser.objects.get(username=request.POST["user"])
        newPost = Post()
        newPost.title = request.POST["title"]
        newPost.topic = Topic.objects.get(id=topic_id)
        newPost.body = request.POST["body"]
        newPost.author = user
        newPost.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)


class TopicListView(ListView):
    model = Topic
    template_name = 'forum.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'topics'

class TopicDetailView(DetailView):
    model = Topic
    template_name_suffix = "-detail"

    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(topic=self.kwargs.get('pk'))
        return context

class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title', 'description']

    def form_valid(self, form):
        return super().form_valid(form)

# Post views
# @login_required(login_url='/todolist/login/')
def create_post_json(request):
    if request.method == "POST":
        post = Post(
            title = request.POST["title"],
            description = request.POST["description"],
            user = request.user,
        )
        task.save()
        return HttpResponse(
            serializers.serialize("json", [task]),
            content_type="application/json",
        )
    return HttpResponse("Invalid method", status_code=405)

class PostDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = Post
    template_name_suffix = "-detail"
    form_class = CreateCommentForm

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.kwargs.get('pk'))
        context['form'] = CreateCommentForm(initial={'post': self.object, 'author': self.request.user})

        return context

    def get_success_url(self):
        return reverse('evorumss:post-detail', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetailView, self).form_valid(form)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name_suffix = "-form"
    fields = ['title', 'body']

    def form_valid(self, form):
        print("in")
        form.instance.author = self.request.user
        form.instance.topic = Topic.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name_suffix = "-form"
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name_suffix = "-confirm-delete"
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False    

# Static pages
