from django.urls import path
from . import views

app_name = "contactus"
urlpatterns = [
    path("", views.contactus_view, name="contactus_page"),
]

