import uuid

from cloudinary.models import CloudinaryField
from django.db import models
from django.urls.base import reverse


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
    songs = models.ManyToManyField(Song)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Record(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video = CloudinaryField('video')
    author = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Records"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("core:record_detail", kwargs={"id": str(self.id)})