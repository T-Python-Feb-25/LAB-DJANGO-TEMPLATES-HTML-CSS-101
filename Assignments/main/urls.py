from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
  path("html/introduction/", views.introduction_view, name="introduction_view"),
  path("css/introduction/", views.Css_introduction_view, name="views.Css_introduction_view"),
  path("article/ai/", views.Article_AI_view, name="Article_AI_view"),
  path("careers/cv/", views.Careers_CV_view, name="Careers_CV_view")
]
