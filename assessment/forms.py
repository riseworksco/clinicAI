import io

from django.http import FileResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from django import forms
from django.conf import settings
from django.forms import ModelForm
from django.template.loader import render_to_string

from assessment.identifiers import Sign
from django.core.mail import send_mail, EmailMessage

from assessment.models import PsychoemotionalScreeningRecord


class StompForm(forms.Form):
    """
    Music Preference Form
    """
    TherapistEmail = forms.EmailField(label='Therapist Email')
    Alternative = forms.IntegerField(label='Alternative', min_value=1, max_value=5)
    Bluegrass = forms.IntegerField(label='Bluegrass', min_value=1, max_value=5)
    Blues = forms.IntegerField(label='Blues', min_value=1, max_value=5)
    Classical = forms.IntegerField(label='Classical', min_value=1, max_value=5)
    Country = forms.IntegerField(label='Country', min_value=1, max_value=5)
    Dance_Electronica = forms.IntegerField(label='Dance/Electronica', min_value=1, max_value=5)
    Folk = forms.IntegerField(label='Folk', min_value=1, max_value=5)
    Funk = forms.IntegerField(label='Funk', min_value=1, max_value=5)
    Gospel = forms.IntegerField(label='Gospel', min_value=1, max_value=5)
    Heavy_Meta = forms.IntegerField(label=' Heavy Meta', min_value=1, max_value=5)
    World = forms.IntegerField(label='World', min_value=1, max_value=5)
    Jazz = forms.IntegerField(label='Jazz', min_value=1, max_value=5)
    New_Age = forms.IntegerField(label='New_Age', min_value=1, max_value=5)
    Oldies = forms.IntegerField(label='Oldies', min_value=1, max_value=5)
    Opera = forms.IntegerField(label='Opera', min_value=1, max_value=5)
    Pop = forms.IntegerField(label='Pop', min_value=1, max_value=7)
    Punk = forms.IntegerField(label='Punk', min_value=1, max_value=7)
    Rap_hip_hop = forms.IntegerField(label='Rap/hip-hop', min_value=1, max_value=7)
    Reggae = forms.IntegerField(label='Reggae', min_value=1, max_value=7)
    Religious = forms.IntegerField(label='Religious', min_value=1, max_value=7)
    Rock = forms.IntegerField(label='Rock', min_value=1, max_value=7)
    Soul_R_B = forms.IntegerField(label=' Soul/R&B', min_value=1, max_value=7)
    Soundtracks_heme_song = forms.IntegerField(label='Soundtracks/theme song', min_value=1, max_value=7)

    def get_info(self):
        form = self
        # rendered_form = form.render("form_snippet.html")
        description = """
                Please indicate your basic preference for each of the following genres using the scale provided.
        1-----------------2-----------------3-----------------4-----------------5-----------------6-----------------7
        Dislike Dislike Dislike a Neither like Like a Like Like
            """
        context = {
            'form': form,
            'header': 'STOMP-Revised',
            'description': description, }

        result = render_to_string('email/stomp.html', context)
        # print(form.data)
        recipient = form.data['TherapistEmail']
        return 'STOMP-Revised', result, recipient

    def send(self):
        subject, msg, recipent = self.get_info()

        send_mail(
            subject=subject,
            message="",
            html_message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipent]
        )


class NeurologicScreeningEvaluationForm(forms.Form):
    TherapistEmail = forms.EmailField(label='Therapist Email')
    feature1 = forms.ChoiceField(label="Feature 1: Acute Onset or Fluctuating Course",
                                 choices=[(Sign.Positive, "Positive"), (Sign.Negative, "Negative")])
    feature1ExistsInEPIC = forms.ChoiceField(label="Exists in Epic",
                                             choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")])
    feature1Single = forms.CharField()
    feature2 = forms.ChoiceField(label="Feature 2: Inattention",
                                 choices=[(Sign.Positive, "Positive"), (Sign.Negative, "Negative")])
    feature2ExistsInEPIC = forms.ChoiceField(label="Exists in Epic",
                                             choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")])
    feature2Single = forms.CharField()
    feature3 = forms.ChoiceField(label="Feature 3: Altered Level of Consciousness",
                                 choices=[(Sign.Positive, "Positive"), (Sign.Negative, "Negative")])
    feature3ExistsInEPIC = forms.ChoiceField(label="Exists in Epic",
                                             choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")])
    feature3Single = forms.CharField()
    feature4 = forms.ChoiceField(label="Feature 4: Disorganized Thinking",
                                 choices=[(Sign.Positive, "Positive"), (Sign.Negative, "Negative")])
    feature4ExistsInEPIC = forms.ChoiceField(label="Exists in Epic",
                                             choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")])
    feature4Single = forms.CharField()

    def get_info(self):
        form = self
        description = """
            """
        context = {
            'form': form,
            'header': 'Neurologic Screening/Evaluation',
            'description': description, }

        result = render_to_string('email/stomp.html', context)
        print(form.data)
        recipient = form.data['TherapistEmail']
        return 'Neurologic Screening/Evaluation', result, recipient

    def send(self):
        subject, msg, recipent = self.get_info()

        # send_mail(
        #     subject=subject,
        #     message="",
        #     html_message=msg,
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=[recipent]
        # )

        email = EmailMessage(
            subject,
            "",
            settings.EMAIL_HOST_USER,
            [recipent],
            reply_to=["another@example.com"],
            headers={"Message-ID": "foo"},
        )


class PrePostForm(forms.Form):
    TherapistEmail = forms.EmailField(label='Therapist Email')
    VITALSExistsInEPIC = forms.ChoiceField(label="Exists in Epic",
                                           choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")])
    VITALSSingle = forms.CharField()

    BPExistsInEPIC = forms.ChoiceField(label="Exists in Epic",
                                       choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")])
    BPSingle = forms.CharField()

    BPLocationExistsInEPIC = forms.ChoiceField(label="Exists in Epic",
                                               choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")])
    BPLocationSingle = forms.CharField()

    PatientPositionExistsInEPIC = forms.ChoiceField(label="Exists in Epic",
                                                    choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")])
    PatientPositionSingle = forms.CharField()

    HRExistsInEPIC = forms.ChoiceField(label="Exists in Epic",
                                       choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")])
    HRSingle = forms.CharField()

    RRExistsInEPIC = forms.ChoiceField(label="Exists in Epic",
                                       choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")])
    RRSingle = forms.CharField()
    # O2
    O2ExistsInEPIC = forms.ChoiceField(label="Exists in Epic",
                                       choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")])
    O2Single = forms.CharField()

    PulseExistsInEPIC = forms.ChoiceField(label="Exists in Epic",
                                          choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")])
    PulseSingle = forms.CharField()

    PulseOxLocationExistsInEPIC = forms.ChoiceField(label="Exists in Epic",
                                                    choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")])
    PulseOxLocationSingle = forms.CharField()

    def get_info(self):
        form = self
        description = """
            """
        context = {
            'form': form,
            'header': 'PrePostForm',
            'description': description, }

        result = render_to_string('email/stomp.html', context)
        print(form.data)
        recipient = form.data['TherapistEmail']
        return 'Pre/Post Tests', result, recipient

    def send(self):
        subject, msg, recipient = self.get_info()

        pdf = self.createPDF(msg)

        email = EmailMessage(
            subject=subject,
            body="",
            from_email=settings.EMAIL_HOST_USER,
            to=[recipient]
        )

        email.attach('generated.pdf', pdf, 'application/pdf')

        email.send(fail_silently=False)

    def createPDF(self, data):
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=A4)
        # Start writing
        c.drawString(100, 500, data)
        # End writing
        c.showPage()
        c.save()
        pdf = buffer.getvalue()
        buffer.close()
        print("pdf generation called")
        return pdf


class PsychoemotionalScreeningEvaluationForm(ModelForm):
    """
    PsychoemotionalScreeningEvaluationForm
    """

    class Meta:
        model = PsychoemotionalScreeningRecord
        fields = ['doctor', 'patient']
