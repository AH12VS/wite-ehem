from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache
from .forms import LoginForm

@never_cache
def login_view(request):
    if request.user.is_authenticated: 
        return redirect("users:user_detail_page")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            user = authenticate(
                request, email=cd["email"], password=cd["passwd"])

            if user != None:
                login(request, user)
                if user.is_active:
                    login(request, user)
                    return redirect("users:user_detail_page")
    else:
        form = LoginForm()
    return render(request, "login/login.html", {"form": form})
