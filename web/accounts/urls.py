from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name = "accounts/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name = "accounts/logout.html"), name='logout'),
]