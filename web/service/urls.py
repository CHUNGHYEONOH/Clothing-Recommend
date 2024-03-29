from django.contrib import admin
from django.conf.urls import url
from django.urls import path, re_path, reverse, include
from service import views

app_name = "service"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recommend/', views.recommend, name='recommend'),
    path('review/', views.review, name='review'),
    path('create_review/', views.create_review, name='create_review'),
]