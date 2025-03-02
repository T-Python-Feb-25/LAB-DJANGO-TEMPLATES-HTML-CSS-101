from . import views
from django.urls import path


app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("ctsv", views.ctsv_view, name="ctsv_view"),
    path("ctsv2", views.Ctsv2_view, name="ctsv_view"),
    path("ai", views.Ai_view, name="Ai_view"),
    path("cv", views.cv_view, name="cv_view")
]