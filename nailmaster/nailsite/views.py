from django.shortcuts import render, redirect
from .models import ImageWorks


def nailsite(request):
    wr = ImageWorks.objects.all()
    context = {
        "nailsite": wr
    }
    return render(request, "nailsite/index.html", context)
