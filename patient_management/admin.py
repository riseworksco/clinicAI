from django.contrib import admin

from patient_management.models import Doctor, Patient

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
