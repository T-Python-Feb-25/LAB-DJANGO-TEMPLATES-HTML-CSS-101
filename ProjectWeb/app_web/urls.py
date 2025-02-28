from django.urls import path
from . import views
app_web = "web"
urlpatterns = [
     path("", views.page_view, name="page_view"),
     path("html/introduction/", views.project_htmlone, name="project_htmlone"),
     path("css/view/" , views.css_view , name="css_view"),
     path("css/introduction/" , views.project_csstwo , name="project_csstwo"),
     path("article/ai/" , views.ai_revolution_project , name="ai_revolution_project"),
     path("careers/cv/" , views.cv_project , name="cv_project"),


]