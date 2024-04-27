from django.contrib.auth.models import User
from django.db import models

from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech

from music_management.models import Playlist


# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    # type1_value = models.CharField('eval', max_length=30, null=True)
    # type1_epic = models.CharField('No', max_length=30,null=True)
    # type1_smf = models.IntegerField(null=True)
    #
    # MusicTherapyCredential = models.CharField('eval', max_length=30,null=True)
    # BachelorDegree = models.CharField('eval', max_length=30, null=True)
    # MastersDegree = models.CharField('eval', max_length=30, null=True)
    # DoctorateDegree = models.CharField('eval', max_length=30, null=True)
    # OtherLicenseCredential = models.CharField('eval', max_length=30, null=True)
    # OtherTrainingDesignation = models.CharField('eval', max_length=30,null=True)
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


# def transcribe(gcs_uri: str = "gs://cloud-samples-data/speech/brooklyn_bridge.raw") -> speech.RecognizeResponse:
def transcribe(
        project_id: str = "sojo-api-380801",
        model: str = "gemini",
        audio_file: str = "gs://cloud-samples-data/speech/brooklyn_bridge.raw",
):
    # Instantiates a client
    client = SpeechClient()

    # Reads a file as bytes
    with open(audio_file, "rb") as f:
        content = f.read()

    config = cloud_speech.RecognitionConfig(
        auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
        language_codes=["en-US"],
        model=model,
    )

    request = cloud_speech.RecognizeRequest(
        recognizer=f"projects/{project_id}/locations/global/recognizers/_",
        config=config,
        content=content,
    )

    # Transcribes the audio into text
    response = client.recognize(request=request)

    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")

    return response


class SessionRecord(models.Model):
    date = models.CharField(max_length=100)
    patient_id = models.IntegerField(blank=False)
    doctor_id = models.IntegerField(blank=False)
    session_id = models.IntegerField(blank=False)
    doctor_name = models.CharField(max_length=100, blank=False)
    notes = models.CharField(max_length=500, blank=False)
    transcripts = models.CharField(max_length=500, blank=False)
    voice_recording_url = models.CharField(max_length=500, blank=False)
