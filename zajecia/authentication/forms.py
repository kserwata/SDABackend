from django import forms


class SimpleUserForm(forms.Form):
    login = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    email = forms.CharField(max_length=30)


class SimpleLoginForm(forms.Form):
    login = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
