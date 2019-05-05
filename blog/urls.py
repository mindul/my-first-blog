# 새 파일 blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
]
