from django import forms
from .models import Review
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields =('userid','image','title','designer','price','score',)
