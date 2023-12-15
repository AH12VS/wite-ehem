from django.urls import path
from . import views

app_name="users"
urlpatterns = [
    path("user/", views.user_detail_view, name="user_detail_page"),
    path("userprofile/<slug:user_id>", views.userprofile_view, name="user_profile_page"),
    # path("userprofile/<int:pk>", views.userprofile_view, name="user_profile_page")
    path("edityouraccount/", views.user_detail_edit_view, name="user_detail_edit_page"),
    path("edityouraccount/changepasswd/", views.user_change_passwd_view, name="user_change_passwd_view_page")
]
