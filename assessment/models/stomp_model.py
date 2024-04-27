import datetime
import logging
from datetime import date

from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string

from patient_management.models import Doctor, Patient


# Create your models here.
class Stomp(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    Alternative = models.IntegerField()
    Bluegrass = models.IntegerField()
    Blues = models.IntegerField()
    Classical = models.IntegerField()
    Country = models.IntegerField()
    Dance_Electronica = models.IntegerField()
    Folk = models.IntegerField()
    Funk = models.IntegerField()
    Gospel = models.IntegerField()
    Heavy_Meta = models.IntegerField()
    World = models.IntegerField()