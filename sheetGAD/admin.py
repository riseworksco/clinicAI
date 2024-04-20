from django.contrib import admin

from .models import GAD7Submission

# Register your models here.

class GAD7SubmissionAdmin(admin.ModelAdmin):
    pass


admin.site.register(GAD7Submission, GAD7SubmissionAdmin)
