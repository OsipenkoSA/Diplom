from django.forms import ModelForm
from .models import Review
from django import forms


class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'review_input'})

    class Meta:
        model = Review
        fields = ['body',]
        labels = {
            'body': 'Добавьте свой отзыв',
        }
