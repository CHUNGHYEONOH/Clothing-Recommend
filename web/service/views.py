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
    review = Review.objects.all()
    return render(request, 'service/review.html', {'review':review})

def create_review(request):
    data = dict()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            Reviews = Review.objects.all()
            data['html_review'] = render_to_string('service/review_list.html', {
                'Reviews': Reviews
            })
        else:
            data['form_is_valid'] = False
    else:
        form = ReviewForm()

    form = ReviewForm()
    context = {'form' : form}
    data['html_form'] = render_to_string('service/create_review.html', context, request = request,)
    return JsonResponse(data)