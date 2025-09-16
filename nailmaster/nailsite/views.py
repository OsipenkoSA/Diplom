from django.shortcuts import render, redirect
from .models import ImageWorks


def index(request):
    return render(request, "nailsite/index.html")


def nailsite(request):
    wr = ImageWorks.objects.all()
    context = {
        "nailsite": wr
    }
    return render(request, "nailsite/work-gallery.html", context)
