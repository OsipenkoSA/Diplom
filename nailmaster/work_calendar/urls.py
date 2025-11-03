from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    # path('event/<int:pk>/', views.event, name='event'),
    # path(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]
