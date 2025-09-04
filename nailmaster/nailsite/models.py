from django.db import models


class ImageWorks(models.Model):
    title = models.CharField(max_length=200)
    images = models.ImageField(upload_to="works/%Y/%m/%d/", blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
