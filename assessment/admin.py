from django.contrib import admin

from .models import (
    GAD2,
    GAD7,
    PHQ2,
    PHQ9,
    AAQ2Model,
    AT4Model,
    CAM1Model,
    CatCatFlowsheetRecord,
    GAD7Model,
    PHQ9Model,
    PsychoemotionalScreeningRecord,
    RASModel,
    Stomp,
)

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


#


admin.site.register(CatCatFlowsheetRecord, CatCatFlowsheetRecordAdmin)


class AT4ModelAdmin(admin.ModelAdmin):
    pass


#


admin.site.register(AT4Model, AT4ModelAdmin)


class AAQ2ModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(AAQ2Model, AAQ2ModelAdmin)


class CAM1ModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(CAM1Model, CAM1ModelAdmin)


# class GAD7ModelAdmin(admin.ModelAdmin):
#    pass


# admin.site.register(GAD7Model, GAD7ModelAdmin)


# class PHQ9ModelAdmin(admin.ModelAdmin):
#    pass


# admin.site.register(PHQ9Model, PHQ9ModelAdmin)


class RASModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(RASModel, RASModelAdmin)
