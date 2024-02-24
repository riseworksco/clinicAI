from django.contrib import admin
from .models import Stomp


# Register your models here.

class StompAdmin(admin.ModelAdmin):
    pass


admin.site.register(Stomp, StompAdmin)
