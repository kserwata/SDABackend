from django.contrib import admin
from .models import Car, Truck


def change_petrol(modeladmin, request, queryset):
    queryset.update(petrol=4)


change_petrol.short_description = "Zmien rodzaj paliwa"


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'petrol', 'year', 'doors']
    ordering = ['-year']
    actions = [change_petrol]


class TruckAdmin(admin.ModelAdmin):
    pass


admin.site.register(Truck, TruckAdmin)
