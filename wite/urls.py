"""
URL configuration for wite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# this lines are added to upload media
from django.conf import settings
from django.conf.urls.static import static

handler404 = "errhandler.views.err_404"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls", namespace="home")),
    path("signin/", include("signin.urls", namespace="signin")),
    path("login/", include("login.urls", namespace="login")),
    path("posts/", include("posts.urls", namespace="posts")),
    path("users/", include("users.urls", namespace="users")),
    path("logout/", include("logout.urls", namespace="logout")),
    path("copyr/", include("copyr.urls", namespace="copyr")),
    path("contactus/", include("contactus.urls", namespace="contactus")),
    path("", include("about.urls", namespace="about")),
    path("jet/", include("jet.urls", "jet")),
    
    path('ckeditor/', include('ckeditor_uploader.urls')), # for CKEditor
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # this line is added to upload media
