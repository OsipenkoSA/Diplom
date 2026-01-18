from django.contrib import admin
from .models import Event


class WorkCalendarAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'start_time')
    fields = ('user', 'title', 'start_time', 'end_time')


admin.site.register(Event, WorkCalendarAdmin)
