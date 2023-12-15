from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import AnonymousUser
from django.utils.text import slugify
from django.contrib.auth import login
from posts.models import PostModel
from .models import UserModel
from .forms import UserDetailEditForm, UserChangePasswdForm

# @login_required("home:home_page")


def user_detail_view(request):
    context = {}
    user = request.user

    if not request.user.is_anonymous:
        user_posts = PostModel.objects.filter(author=user)
        context = {
            "user": user,
            "posts": user_posts,
        }
    else:
        return redirect("login:login_page")

    return render(request, "users/user-detail.html", context)


def user_detail_edit_view(request):
    context = {}
    user = request.user

    if not request.user.is_anonymous:
        if request.method == "POST":
            # request.FILES is used to upload media
            form = UserDetailEditForm(request.POST, request.FILES)
            if form.is_valid():
                cd = form.cleaned_data
                user.full_name = cd["fullname"]
                user.age = cd["age"]
                user.sex = request.POST.get("sex")
                user.bio = cd["bio"]
                if cd["image_prof"] != None:
                    user.image_prof = cd["image_prof"]
                user.save()
                
                return redirect("users:user_detail_page")
        else:
            form = UserDetailEditForm()

        context = {
            "user": user,
            "form": form,
        }
    else:
        return redirect("login:login_page")

    return render(request, "users/user-detail-edit.html", context)


def user_change_passwd_view(request):
    user = request.user
    if not request.user.is_anonymous:
        if request.method == "POST":
            form = UserChangePasswdForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                old_passwd = cd["old_passwd"]
                new_passwd = cd["new_passwd"]
                confrim_new_passwd = cd["confrim_new_passwd"]

                if not user.check_password(old_passwd):
                    return redirect("users:user_change_passwd_view_page")

                user.set_password(new_passwd)

                user.save()

                login(request, user)

                return redirect("users:user_detail_page")
        else:
            form = UserChangePasswdForm()
        context = {
            "user": user,
            "form": form,
        }
    else:
        return redirect("login:login_page")

    return render(request, "users/user-change-passwd.html", context)


def userprofile_view(request, user_id):
    user = get_object_or_404(UserModel, user_unique_id=user_id)

    if request.user == user:
        return redirect("users:user_detail_page")

    user_posts = PostModel.objects.filter(status="published", author=user)

    context = {
        "user": user,
        "posts": user_posts,
    }

    return render(request, "users/user-profile.html", context)
