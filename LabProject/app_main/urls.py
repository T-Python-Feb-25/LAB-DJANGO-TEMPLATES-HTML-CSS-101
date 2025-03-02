from django.urls import path
from . import views



app_name = "app_main"

urlpatterns = [
path("html/introduction/", views.first_html_page, name="first_html_page"),
path("css/introduction/", views.css_view, name="css_view"),
path("article/ai/", views.Ai_view, name="Ai_view"),
path("careers/cv/", views.cv_view, name="cv_view"),
path("cafee/main/", views.cafee_view, name="cafee_view"),
path("cafee/menu/", views.menu_view, name="menu_view"),
path("cafee/det/", views.det_view, name="det_view"),
path("cafee/try/", views.caffee, name="caffee"),
path("theme/store/", views.store_view, name="store_view"),



]
