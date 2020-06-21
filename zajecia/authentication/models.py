from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    telephone = models.IntegerField(default=0)
    location = models.CharField(default="", max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
