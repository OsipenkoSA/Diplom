from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nailsite/', views.nailsite, name='nailsite'),
    path('login/', views.login_user, name='loginuser'),
    path('logout/', views.logout_user, name='logoutuser'),
]
