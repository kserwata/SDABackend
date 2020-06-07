from django import template
from fleet.models import PETROL_CHOISES

register = template.Library()


@register.filter(name="brand_new_car")
def brand_new_car(value):
    if value > 2015:
        return "Nowy pojazd"
    else:
        return "Stary pojazd"


@register.filter(name="test")
def test(value, x):
    return value - x


@register.simple_tag
def mult(a, b):
    return a * b


@register.filter(name="petrol_name")
def petrol_name(value):
    return PETROL_CHOISES[value - 1][1]
