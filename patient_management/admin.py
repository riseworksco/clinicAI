from django.contrib import admin

from patient_management.models import Doctor, Patient, SessionRecord

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(SessionRecord)
