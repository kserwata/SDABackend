from django.views import View
from .models import Car, PETROL_CHOISES
from django.shortcuts import render, redirect
from .forms import SimpleCarForm, ModelCarForm
from django.contrib.auth.mixins import LoginRequiredMixin


class WidokFormularza(LoginRequiredMixin, View):
    login_url = "/authentication/login"

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
        cars = Car.objects.all()
        return render(request, "fleet/lista.html", {
            "elements": cars,
            "formularz": form
        })
