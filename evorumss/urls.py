from django.contrib import admin
from django.urls import path

from .views import *

app_name = 'evorumss'

urlpatterns = [
    path('', TopicListView.as_view(), name='forum-index'),
    path('topic/add/', TopicCreateView.as_view(), name='topic-add'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),
    path('topic/<int:pk>/newpost/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # path('get_all_forum/', get_all_forum, name='get_all_forum'),
    # path('get_all_forum/<str:topic>', get_all_forum_by_topic, name='get_all_forum_by_topic'),
    # path('forum/comment/<int:forum_id>', get_comment, name='get_comment'),
    path('json-post/', show_json_post, name='show_json_post'),
    path('json-comment/', show_json_comment, name='show_json_comment'),
    path('json-topic/', show_json_topic, name='show_json_topic'),
    path('json-post/<int:topic>/', show_json_post_by_topic, name='show_json_post_by_topic'),
    path('forum/comment/<int:post_id>', get_comment, name='get_comment'),
    path('forum/<int:post_id>/comment/add', add_comment, name='add_comment'),
    path('forum/<int:topic_id>/post/add', add_post, name='add_post'),
]