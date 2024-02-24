from django.contrib import admin
from .models import Stomp
from .models import GAD2
from .models import GAD7
from .models import PHQ2
from .models import PHQ9
from .models import PsychoemotionalScreeningRecord
from .models import CatCatFlowsheetRecord


# Register your models here.

class StompAdmin(admin.ModelAdmin):
    pass


admin.site.register(Stomp, StompAdmin)


class GAD2Admin(admin.ModelAdmin):
    pass


admin.site.register(GAD2, GAD2Admin)


class GAD7Admin(admin.ModelAdmin):
    pass


admin.site.register(GAD7, GAD7Admin)


class PHQ2Admin(admin.ModelAdmin):
    pass


admin.site.register(PHQ2, PHQ2Admin)


class PHQ9Admin(admin.ModelAdmin):
    pass


admin.site.register(PHQ9, PHQ9Admin)


class PsychoemotionalScreeningRecordAdmin(admin.ModelAdmin):
    pass


admin.site.register(PsychoemotionalScreeningRecord, PsychoemotionalScreeningRecordAdmin)


class CatCatFlowsheetRecordAdmin(admin.ModelAdmin):
    pass


admin.site.register(CatCatFlowsheetRecord, CatCatFlowsheetRecordAdmin)
