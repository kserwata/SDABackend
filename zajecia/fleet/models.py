from django.db import models

PETROL_CHOISES = (
    (1, 'LPG'),
    (2, 'DIESEL'),
    (3, 'ELECTRIC'),
    (4, 'HYBRID')
)


class Car(models.Model):

    brand = models.CharField(max_length=12, default="Brand")
    petrol = models.IntegerField(choices=PETROL_CHOISES, default=1)
    model = models.CharField(max_length=32)
    year = models.IntegerField()
    doors = models.IntegerField(default=5)

    def __str__(self):
        return "%s %s (%i)" % (self.brand, self.model, self.year)

    def calculate_fuel_consumption(self):
        return self.petrol * self.year


class Truck(models.Model):
    load = models.IntegerField()
