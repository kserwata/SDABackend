from django.views import View
from .models import Car, PETROL_CHOISES
from django.shortcuts import render, redirect
from django.views.generic import ListView


class FleetView(View):

    def get(self, request, *args, **kwargs):
        cars = Car.objects.all()
        return render(request, "fleet/lista.html", {
            "elements": cars,
            "petrol_choises": PETROL_CHOISES
        })

    def post(self, request, *args, **kwargs):
        car = Car(
            brand=request.POST['brand'],
            model=request.POST['model'],
            petrol=request.POST['petrol'],
            year=request.POST['year'],
            doors=request.POST['doors']
        )
        car.save()
        return redirect("fleet_list")

