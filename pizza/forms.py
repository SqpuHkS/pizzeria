from django import forms
from django.core.exceptions import ValidationError

from .models import *


class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        exclude = ['']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form__control'}),
            'price': forms.NumberInput(attrs={'class': 'form__control', 'step':'0.1'}),
            'group': forms.Select(attrs={'class': 'form__control'}),
        }

    def clean_name(self):
        new_name = self.cleaned_data['name'].capitalize()
        if Ingredient.objects.filter(name__iexact=new_name).count():
            raise ValidationError(f'Ingredient must be unique. We have "{new_name}" already')
        return new_name


