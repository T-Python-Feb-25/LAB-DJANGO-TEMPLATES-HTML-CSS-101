# home/urls.py
from django.urls import path
from . import views
from .views import send_email

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('articles/', views.articles, name='articles'),
    path('contact/', views.contact, name='contact'),
    path('send-email/', send_email, name='send_email'),
]
