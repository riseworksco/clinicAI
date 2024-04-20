from django.contrib import admin

from .models import Playlist, Record, Song

# Register your models here.


class SongAdmin(admin.ModelAdmin):
    pass


class PlaylistAdmin(admin.ModelAdmin):
    pass


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("id", "video")


admin.site.register(Song, SongAdmin)
admin.site.register(Playlist, PlaylistAdmin)
