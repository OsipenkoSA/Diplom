from django.shortcuts import render, redirect
from .models import ImageWorks, Services


def index(request):
    services = Services.objects.all()
    context = {
        "services": services
    }
    return render(request, "nailsite/index.html", context)


def nailsite(request):
    wr = ImageWorks.objects.all()
    context = {
        "nailsite": wr
    }
    return render(request, "nailsite/work-gallery.html", context)
