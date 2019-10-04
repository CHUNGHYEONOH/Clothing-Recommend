from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
    post_list = Post.objects.all()
    return render(request, 'service/index.html',{
        'post_list': post_list, 
    })

def post_new(request):
    return render(request, 'service/post_form.html')

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'service/post_detail.html',{
        'post':post,
    })

def mypage(request):
    return render(request, 'service/mypage.html')

def recommend(request):
    return render(request, 'service/recommend.html')

def review(request):
    return render(request, 'service/review.html')