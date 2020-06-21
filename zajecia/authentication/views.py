from django.shortcuts import render, redirect
from .forms import SimpleUserForm, SimpleLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def register_view(request):

    user_form = SimpleUserForm()

    if request.method == "POST":
        user_form = SimpleUserForm(request.POST)
        if user_form.is_valid():
            user = User.objects.create_user(
                user_form.cleaned_data['login'],
                user_form.cleaned_data['email'],
                user_form.cleaned_data['password']
            )
            user.save()
            user_form = SimpleUserForm()

    return render(request, "authentication/register.html", {
        "user_form": user_form
    })


def login_view(request):

    login_form = SimpleLoginForm()

    if request.method == "POST":
        login_form = SimpleLoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username=login_form.cleaned_data['login'], password=login_form.cleaned_data['password'])
            if not user is None:
                login(request, user)
                return redirect("/fleet")

    return render(request, "authentication/login.html", {
        "login_form": login_form
    })


def logout_view(request):
    logout(request)
    return redirect(login_view)
