from django.shortcuts import render


def copyr_view(request):
    return render(request, "copyr/copyr.html", {})

