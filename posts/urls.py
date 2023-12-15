from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path("posts/", views.posts_view, name="posts_page"),
    path("posts/<slug:tag_slug>/", views.posts_view, name="posts_filter_tag_page"),
    path("postdetail/<slug:slug>/<int:pk>/", views.postdetail_view, name="postdetail_page"),
    path("addpost/", views.add_post_view, name="add_post_page"),
    path("search/", views.search_view, name="search_page"),
    path("edit/<slug:slug>/<int:pk>", views.postdetail_edit_view, name="postdetail_edit_page"),
]
