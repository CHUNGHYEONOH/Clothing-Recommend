from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from .models import Review
from .forms import ReviewForm

# Create your views here.

def mypage(request):
    return render(request, 'service/mypage.html')

def recommend(request):
    return render(request, 'service/recommend.html')

def review(request):
    reviews = Review.objects.all()
    return render(request, 'service/review.html', {'reviews':reviews})

def create(requset):
    form = ReviewForm()
    context = {'form' : form}
    html_form = render_to_string('service/create.html',
        context,
        request = request,
    )
    return JsonResponse({'html_form':html_form})