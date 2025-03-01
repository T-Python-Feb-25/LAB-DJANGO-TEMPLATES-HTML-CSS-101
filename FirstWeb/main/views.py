from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html')

def hobbies(request):
    return render(request, 'main/hobbies.html')

def css_introduction(request):
    return render(request, 'main/css_introduction.html')

def ai_article(request):
    return render(request, 'main/ai_article.html')
def cv(request):
    return render(request, 'main/cv.html')

# Create your views here.
