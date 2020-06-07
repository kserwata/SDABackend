from django.db import models
from .validators import first_brand_letter_uppercase
from django.core.exceptions import ValidationError

PETROL_CHOISES = (
    (1, 'LPG'),
    (2, 'DIESEL'),
    (3, 'ELECTRIC'),
    (4, 'HYBRID')
)


class Car(models.Model):

    brand = models.CharField(max_length=12, default="Brand", validators=[first_brand_letter_uppercase])
    petrol = models.IntegerField(choices=PETROL_CHOISES, default=1)
    model = models.CharField(max_length=32)
    year = models.IntegerField()
    doors = models.IntegerField(default=5)

    def validate_unique(self, exclude=None):
        super(Car, self).validate_unique(exclude)
        if self.year < 2005 and self.petrol == 3:
            raise ValidationError('Electric car cannot be older than 2005', code='CarValidator.ElectricCarTooOld')

    def __str__(self):
        return "%s %s (%i)" % (self.brand, self.model, self.year)

    def calculate_fuel_consumption(self):
        return self.petrol * self.year


class Truck(models.Model):
    load = models.IntegerField()
