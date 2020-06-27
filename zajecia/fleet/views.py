from django.views import View
from django.shortcuts import render, HttpResponse
from .forms import SimpleCarForm, ModelCarForm
from .service import FleetService
from django.contrib.auth.mixins import LoginRequiredMixin
import json


class WidokFormularza(View):

    def get(self, request):
        form = ModelCarForm()
        return self.render_view(request, form)

    def post(self, request):
        form = ModelCarForm(request.POST)
        if form.is_valid():
            form.save()
            form = ModelCarForm()
        return self.render_view(request, form)

    def render_view(self, request, form):
        fleet_service = FleetService(request)
        cars = fleet_service.get_all_cars()
        return render(request, "fleet/lista.html", {
            "elements": cars,
            "formularz": form
        })


class ApiView(View):

    def get(self, request):
        fleet_service = FleetService(request)
        cars = fleet_service.get_all_cars()
        json_data = [{"brand": car.brand, "year": car.year, "id": car.pk} for car in cars]
        return HttpResponse(json.dumps(json_data))
