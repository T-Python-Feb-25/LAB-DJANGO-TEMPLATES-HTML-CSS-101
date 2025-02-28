from . import views
from django.urls import path

urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('lab1/',views.lab1_view,name='lab1_view'),
    path('lab2/',views.lab2_view,name='lab2_view'),
    path('second/',views.second_view,name='second_view'),
    path('theme_store/',views.theme_store_view,name='theme_store_view')
]
