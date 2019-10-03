from django.contrib import admin
from django.urls import path, re_path, reverse, include
from service import views

app_name = "service"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainpage/', views.mainpage, name ='main'),
    path('accounts/', include('accounts.urls')),
]
