from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login as django_login, logout as django_logout, authenticate

def signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.signup()
            return render(request, 'service/review.html')
    else:
        signup_form = SignupForm()

    context = {
        'signup_form': signup_form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(
                username=username,
                password=password
            )
            if user:
                django_login(request, user)
                return redirect('mypage')
            login_form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다')
    else:
        login_form = LoginForm()
    context = {
        'login_form': login_form,
    }
    return render(request, 'accounts/login.html', context)