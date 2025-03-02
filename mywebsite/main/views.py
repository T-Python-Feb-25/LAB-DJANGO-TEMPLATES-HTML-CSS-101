from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main:contact.html')

def projects(request):
    return render(request, 'main/projects.html') 

def project_detail(request, project_id):
    return render(request, 'project_detail.html', {'project_id': project_id})  
def cv(request):
    return render(request, 'main/cv.html')

def styled(request):
    return render(request, 'main:style.html')

"""def home(request):
    return render(request, 'main/index.html') """ 


def ai(request):
    return render(request, 'main/ai.html') 






from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # طباعة البيانات في التيرمنال للتأكد من استقبالها
        print(f"Received message from {name} ({email}): {message}")

        return HttpResponse("<h1>✅ Thank you! Your message has been sent.</h1>")

    return render(request, "main/contact.html")
