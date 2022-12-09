from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


plate_number_license = RegexValidator("^[A-Z]{3}[-][0-9]{4}$", message = "Plate number not allowed")

class Parking(models.Model):
    plate_number = models.CharField(max_length=8, blank=True, validators=[plate_number_license])
    time = models.TimeField(auto_now_add=True, null=True, blank=True)
    paid = models.BooleanField(default=True, null=False, blank=False)
    left = models.BooleanField(default=True, null=False, blank=False)
    