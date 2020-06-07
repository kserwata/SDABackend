from django.views import View
from .models import Car, PETROL_CHOISES
from django.shortcuts import render, redirect
from .forms import SimpleCarForm


class FleetView(View):

    def get(self, request, *args, **kwargs):
        cars = Car.objects.all()
        form = SimpleCarForm()
        return render(request, "fleet/lista.html", {
            "elements": cars,
            "petrol_choises": PETROL_CHOISES,
            "form": form
        })

    def post(self, request, *args, **kwargs):
        form = SimpleCarForm(request.POST)
        if form.is_valid():
            car = Car(
                brand=form.cleaned_data['brand'],
                model=form.cleaned_data['model'],
                petrol=1,
                year=1,
                doors=1
            )
            car.save()
        return redirect("fleet_list")

