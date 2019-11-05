from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from .models import Review
from .forms import ReviewForm
from .recommend import Recommend

# Create your views here.

def recommend(request):
    rec = Recommend()
    name = str(request.user)
    try:
        recommend = rec.get_recommend_list(name)
        print(recommend)
        return render(request, 'service/recommend.html', {'recommend':recommend})
    except:
        print("no data")
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
            data['html_review'] = render_to_string('service/review.html', {
                'Reviews': Reviews
            })
        else:
            data['form_is_valid'] = False
    else:
        form = ReviewForm()
    print(request.user)
    form = ReviewForm()
    context = {'form' : form}
    data['html_form'] = render_to_string('service/create_review.html', context, request = request,)
    return JsonResponse(data)