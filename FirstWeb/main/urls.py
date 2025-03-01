from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.home, name='home'),
    path('html/introduction/', views.hobbies, name='hobbies'),
    path('css/introduction/', views.css_introduction, name='css_introduction'),
    path('article/ai/', views.ai_article, name='ai_article'),
    path('careers/cv/', views.cv, name='cv'),
]