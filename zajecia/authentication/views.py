from django.shortcuts import render, redirect, HttpResponse
from .forms import SimpleUserForm, SimpleLoginForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required


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
    logout(request)
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
    login(request, user)
    return redirect("/fleet")
