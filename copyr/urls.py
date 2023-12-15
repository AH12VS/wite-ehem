from django.urls import path
from . import views

app_name = "copyr"
urlpatterns = [
    path("", views.copyr_view, name="copyr_page"),
]
