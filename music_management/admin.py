from django.contrib import admin
from .models import Song, Playlist


# Register your models here.

class SongAdmin(admin.ModelAdmin):
    pass


class PlaylistAdmin(admin.ModelAdmin):
    pass


admin.site.register(Song, SongAdmin)
admin.site.register(Playlist, PlaylistAdmin)
