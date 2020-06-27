from .models import Car


class FleetService:

    def __init__(self, request):
        self.__request = request

    def get_all_cars(self):
        cars = Car.objects.filter(year__gt=2010)
        return cars
