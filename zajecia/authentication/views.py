from django.shortcuts import render, redirect, HttpResponse
from .forms import SimpleUserForm, SimpleLoginForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required
import jwt
import datetime
import json


def index_page(request):
    return HttpResponse("index")


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
            group = Group.objects.get(name="Uzytkownicy")
            user.groups.add(group)
            user_form = SimpleUserForm()

    return render(request, "authentication/register.html", {
        "user_form": user_form
    })


def login_view(request):

    login_form = SimpleLoginForm()

    if request.method == "POST":
        if request.META['CONTENT_TYPE'] == "application/json":
            data = json.loads(request.body)
            username = data['login']
            password = data['password']
            user = User.objects.get(username=username)
            if user.check_password(password):
                payload = {
                    "username": username,
                    "expire": datetime.datetime.now().timestamp() + 3600
                }
                return HttpResponse(jwt.encode(payload, "test123"))
        else:
            login_form = SimpleLoginForm(request.POST)
            if login_form.is_valid():
                user = authenticate(username=login_form.cleaned_data['login'], password=login_form.cleaned_data['password'])
                if not user is None:
                    login(request, user)
                    if request.GET.get("next"):
                        return redirect(request.GET['next'])
                    return redirect("/")

    return render(request, "authentication/login.html", {
        "login_form": login_form
    })


def logout_view(request):

    last_user = request.session.get("current_user")

    logout(request)

    if last_user:
        user = User.objects.get(pk=last_user)
        login(request, user)
        return redirect(users)

    return redirect(login_view)


def users(request):
    if not request.user.is_superuser:
        return redirect(logout_view)

    users = User.objects.all()

    return render(request, "authentication/users.html", {
        "users": users
    })


def login_as(request, pk):
    if not request.user.is_superuser:
        return redirect(logout_view)

    user = User.objects.get(pk=pk)

    current_user = request.user

    login(request, user)

    request.session['current_user'] = current_user.pk
    return redirect("/fleet")
