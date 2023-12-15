from django.shortcuts import render, redirect
from .forms import ContactusForm
from .savem import check_dirs, save_mail


def contactus_view(request):
    if request.method == "POST":
        form = ContactusForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            fullname = cd["fullname"]
            email = cd["email"]
            subject = cd["subject"]
            message = cd["message"]

            check_dirs(cd["subject"])
            save_mail(dir=cd["subject"], msg=message, subject=subject, name=f"{fullname}:{email}")

            return redirect("home:home_page")
    else:
        form = ContactusForm()

    context = {
        "form": form,
    }

    return render(request, "contactus/contactus.html", context)
