from django.shortcuts import render, redirect
from .models import ImageWorks, Services, Review
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import ReviewForm, TelebotForm
from django.contrib import messages
from django.core.paginator import Paginator
from telebot.sendmessage import send_telegram


def index(request):
    services = Services.objects.all()
    form = TelebotForm()
    context = {
        "services": services,
        "form": form
    }
    return render(request, "nailsite/index.html", context)


def nailsite(request):
    wr = ImageWorks.objects.all()
    context = {
        "nailsite": wr,
    }
    paginator = Paginator(wr, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context.update({'nailsite': page_obj})

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


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')


def review_user(request):
    reviews = Review.objects.all()
    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.owner = request.user
        review.save()
        return redirect('review')

    context = {
        'form': form,
        'reviews': reviews
    }

    paginator = Paginator(reviews, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context.update({'reviews': page_obj})

    return render(request, 'nailsite/review.html', context)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        send_telegram(tg_name=name, tg_phone=phone)
        return render(request, 'nailsite/thanks.html', {'name': name})
    else:
        return render(request, 'nailsite/thanks.html')


def about(request):
    return render(request, 'nailsite/about.html', {'about': about})

