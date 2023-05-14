from django.forms import ModelForm
from django import forms
from .models import MiesOpskrifter

class UploadForm(ModelForm):
    CATEGORY_CHOICES = [
        ('Snacks', 'Snacks'),
        ('Forret', 'Forret'),
        ('Hovedret', 'Hovedret'),
        ('Salat', 'Salat'),
        ('Tilbehør', 'Tilbehør'),
        ('Brød', 'Brød'),
        ('Tapas', 'Tapas'),
        ('Søde sager', 'Søde sager'),
        ('Drinks', 'Drinks'),
        ('Andet', 'Andet'),
    ]
    KITCHEN_CHOICES = [
        ('Asiatisk', 'Asiatisk'),
        ('Fransk', 'Fransk'),
        ('Italiensk', 'Italiensk'),
        ('Nordisk', 'Nordisk'),
        ('Spansk', 'Spansk'),
        ('Amerikansk', 'Amerikansk'),
        ('Fusion', 'Fusion'),
        ('Bagværk', 'Bagværk'),
        ('Drinks', 'Drinks'),
        ('Andet', 'Andet'),
    ]
    title = forms.CharField()
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, initial='option1')
    kitchen = forms.ChoiceField(choices=KITCHEN_CHOICES, initial='option1')
    link = forms.CharField()

    class Meta:
        model = MiesOpskrifter
        fields = ['title', 'category', 'kitchen', 'link']
