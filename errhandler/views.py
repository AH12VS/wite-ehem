from django.shortcuts import render

def err_404(request, exception):
    return render(request, "errhandler/404.html", status=404)
