from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def articles(request):
    return render(request, 'home/articles.html')

def contact(request):
    return render(request, 'home/contact.html')

@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')

            if name and email and message:
                # Send email
                send_mail(
                    f'Message from {name}',
                    message,
                    email,
                    ['elafabdualrhman00@gmail.com'], # Replace with your email
                    fail_silently=False,
                )
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Invalid form data'})
        except json.JSONDecodeError as e:
            print(f"JSONDecodeError: {e}")
            return JsonResponse({'success': False, 'error': 'Invalid JSON'})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})
