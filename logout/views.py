from django.shortcuts import render, redirect
from django.contrib.auth import logout
# from django.contrib.auth.decorators import login_required
# from users.models import UserModel


def logout_view(request):
    logout(request)
    return redirect("home:home_page")
    # return render(request, "logout/logout.html", {})
