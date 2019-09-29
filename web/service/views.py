from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'service/index.html')

def post_new(request):
    return render(request, 'service/post_form.html')
    