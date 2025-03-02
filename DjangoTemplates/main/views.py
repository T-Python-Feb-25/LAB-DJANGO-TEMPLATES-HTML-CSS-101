from django.shortcuts import render


def home_view(request):
    return render(request,'main/home.html/')

def lab1_view(request):
    return render(request,'main/lab1.html')
def lab2_view(request):
    return render(request,'main/lab2.html')
def ai_view(request):
    return render(request, 'main/ai.html')
def cv_view(request):
    return render(request,'main/cv.html')
def second_view(request):
    return render(request,'main/test2.html/')
def theme_store_view(request):
    return render(request,'main/theme_store.html')