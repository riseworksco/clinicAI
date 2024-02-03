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

    type1_value = models.CharField('eval', max_length=30)
    type1_epic = models.CharField('No', max_length=30)
    type1_smf = models.IntegerField()

    MusicTherapyCredential = models.CharField('eval', max_length=30)
    BachelorDegree = models.CharField('eval', max_length=30)
    MastersDegree = models.CharField('eval', max_length=30)
    DoctorateDegree = models.CharField('eval', max_length=30)
    OtherLicenseCredential = models.CharField('eval', max_length=30)
    OtherTrainingDesignation = models.CharField('eval', max_length=30)
    # JobTitleType: Director / Admin. / Supervisor, Music
    # Therapist
    # Age
    # Range
    # Served: Infants / Young
    # children(birth - 3), Children(4 - 7)
    # Settings
    # Served: Children
    # 's Day Care/Preschool,Community Based Service,Day Care/Treatment Center,Early Intervention Program,Private Music Therapy Agency
    # Populations
    # Served: Autism
    # Spectrum, Developmentally
    # Disabled, Dual
    # Diagnosed, Early
    # Childhood, Learning
    # Disabled, Multiply
    # Disabled, Music
    # Therapy
    # College
    # Students

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
