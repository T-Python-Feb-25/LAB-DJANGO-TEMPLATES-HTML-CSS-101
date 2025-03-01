from django.urls import path
from . import views

main = "name"

urlpatterns = [
    path("intro/to/html", views.introToHTML, name="intro_to_html"),
    path("intro/to/css", views.introToCSS, name="intro_to_css"),
    path("article/ai", views.articleAi, name="article-ai"),
    path("career/cv", views.careercv, name="career-cv")

]
