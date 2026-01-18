from django.db import models
from django.contrib.auth.models import User


class ImageWorks(models.Model):
    title = models.CharField(max_length=200)
    images = models.ImageField(upload_to="works/%Y/%m/%d/", blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "фото"
        verbose_name_plural = "фото"


class Services(models.Model):
    title = models.CharField(max_length=200)
    images = models.ImageField(upload_to="services/", blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "услуга"
        verbose_name_plural = "услуги"


class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.created

    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"
