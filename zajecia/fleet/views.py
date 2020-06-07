from django.views import View
from .models import Car, PETROL_CHOISES
from django.shortcuts import render, redirect
from .forms import SimpleCarForm, ModelCarForm


class FleetView(View):

    def get(self, request, *args, **kwargs):
        cars = Car.objects.all()
        form = ModelCarForm(instance=cars.first())
        return render(request, "fleet/lista.html", {
            "elements": cars,
            "petrol_choises": PETROL_CHOISES,
            "formularz": form
        })

    def post(self, request, *args, **kwargs):
        form = ModelCarForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("fleet_list")

