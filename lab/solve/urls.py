from django.urls import path
from . import views

app_name = 'solve'

urlpatterns = [
path('',views.main,name="main"),
path('html/introduction/',views.task1,name="task1"),
path('css/introduction/',views.task2,name="task2"),
path('article/ai/',views.task3,name="task3"),
path('careers/cv/',views.cv,name="cv")
]