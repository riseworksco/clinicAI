from django.forms import ModelForm
from patient_management.models import SessionRecord


class SessionRecordForm(ModelForm):
    """
    PsychoemotionalScreeningEvaluationForm
    """

    class Meta:
        model = SessionRecord
        fields = ["start_time", "end_time", "doctor", "patient", "notes", "transcripts","voice_recording_url"]
