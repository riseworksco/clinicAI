from django.db import models


# Create your models here.
class Song(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100, null=True)
    youtube_link = models.CharField(max_length=100, null=True)
    music_link = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Playlist(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, null=True)
    songs = models.ManyToManyField(Song, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
