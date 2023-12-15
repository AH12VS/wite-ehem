from django.urls import path
from . import views

app_name = "about"

urlpatterns = [
    path("about/", views.about_view, name="about_page"),
]
