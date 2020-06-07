from django.views import View
from .models import Car, PETROL_CHOISES
from django.shortcuts import render, redirect
from .forms import SimpleCarForm, ModelCarForm


def form_view(request):

    form = ModelCarForm()

    if request.method == "POST":
        form = ModelCarForm(request.POST)

        if form.is_valid():
            form.save()

    cars = Car.objects.all()

    return render(request, "fleet/lista.html", {
        "elements": cars,
        "formularz": form
    })

