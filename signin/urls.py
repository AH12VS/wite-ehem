from django.urls import path
from . import views

app_name = "signin"
urlpatterns = [
    path("", views.signin_view, name="signin_page"),
    path("validate/<int:pk>", views.validate_account_view,
         name="validate_account_page"),
]
