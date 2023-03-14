from django.contrib.auth.models import User
from django.db import models

from music_management.models import Playlist


# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username
