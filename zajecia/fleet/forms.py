from django import forms


class SimpleCarForm(forms.Form):
    brand = forms.CharField(max_length=30)
    model = forms.CharField(max_length=30)
