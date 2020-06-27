from .models import Car


class FleetService:

    def __init__(self, request):
        self.__request = request

    def get_all_cars(self):
        cars = Car.objects.all()
        return cars
