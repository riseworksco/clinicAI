from django.contrib import admin

from patient_management.models import Patient, Doctor

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
