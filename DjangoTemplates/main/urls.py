from . import views
from django.urls import path

urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('lab1/',views.lab1_view,name='lab1_view'),
    path('lab2/',views.lab2_view,name='lab2_view'),
    path('second/',views.second_view,name='second_view'),
    path('article/ai/',views.ai_view,name='ai_view'),
    path('careers/cv/',views.cv_view,name='cv_view')
]
