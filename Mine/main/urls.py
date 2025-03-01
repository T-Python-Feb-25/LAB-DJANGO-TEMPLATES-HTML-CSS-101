from django.urls import path
from . import views

app_name= "main"

urlpatterns = [

     path("html/introduction/", views.introduction, name = "introduction"),
     path("css/introduction/", views.style_intro, name = "style_intro"),
     path("article/ai/", views.article_ai, name ="article_ai"),
     path("cv/",views.cv, name = "cv")
]