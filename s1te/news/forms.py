from .models import Articles
from django.forms import ModelForm, DateTimeInput, Textarea, TextInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article name',
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons Article',
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Publish date',
            }),
            "full_text": Textarea(attrs={
                'class': 'Text stat`i',
                'placeholder': 'Text stat`i',
            })
        }