from django.db import models

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
