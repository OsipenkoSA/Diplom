from django.shortcuts import render, redirect
from .models import ImageWorks, Services
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


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


def login_user(request):
    if request.method == "GET":
        return render(request, 'nailsite/loginuser.html', {"form": AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'nailsite/loginuser.html',
                          {"form": AuthenticationForm(), 'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('index')
