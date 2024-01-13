from django.contrib import admin
from .models import Stomp, GAD2


# Register your models here.
# Register your models here.

class StompAdmin(admin.ModelAdmin):
    pass


class GAD2Admin(admin.ModelAdmin):
    pass


admin.site.register(Stomp, StompAdmin)
admin.site.register(GAD2, GAD2Admin)
