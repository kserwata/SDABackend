from django import forms
from .models import Car


class SimpleCarForm(forms.Form):
    brand = forms.CharField(max_length=30)
    model = forms.CharField(max_length=30)


class ModelCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'