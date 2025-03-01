from django.urls import path
from . import views
app_name="main"
urlpatterns=[
    path("html/introduction/",views.favourite_team_view,name="favourite_team"),
    path("learn/",views.learn_view,name="learn_view"),
    path("learn/form/",views.form_practice_view,name="form_practice_view"),
    path("learn/ccs/",views.ccs_practice_view,name="ccs_practice_view"),
    path("css/introduction/",views.css_introduction_view,name="css_introduction.view"),
    path("article/ai/",views.ai_revolution_view,name="ai_revolution_view"),
    path("careers/cv/",views.careers_cv_view,name="careers_cv_view"),
    path("themestore/",views.theme_store_view,name="theme_store_view")

]