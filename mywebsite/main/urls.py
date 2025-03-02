from django.urls import path
from .views import home, about, contact, projects, project_detail, cv, styled, ai

app_name="main"

urlpatterns = [
    path('',home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('projects/', projects, name='projects'),
    path('projects/<int:project_id>/', project_detail, name='project_detail'), 
    path('cv/', cv, name='cv'),
    path('styled/', styled, name='styled'),
    path('ai/', ai, name='ai'),
]
