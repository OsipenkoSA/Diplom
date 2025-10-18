from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # @property
    # def get_html_url(self):
    #     url = reverse('calendar:event_edit', args=(self.id,))
    #     return f'<a href="{url}"> {self.title} </a>'
