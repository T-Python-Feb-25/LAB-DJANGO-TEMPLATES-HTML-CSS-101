from django.urls import path
from . import views
app_name = "learning"

urlpatterns = [
    path("", views.HTML_view, name="HTML_view"),
    path("css/introduction/", views.CSS_view, name="CSS_view"),
    path("article/ai/", views.AI_view, name="AI_view"),
    path("careers/cv/", views.CV_view, name="CV_view"),

]