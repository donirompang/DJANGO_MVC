from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('input_blog/', views.input_blog, name='input_blog'),
    path('<int:blog_id>', views.blog_detail, name='blog_detail'),
]
