import datetime
import logging

from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string


class ATModel(models.Model):
    patientName = models.CharField(max_length=255)
    patientNumber = models.CharField(max_length=255)
    birthDate = models.DateField(default=datetime.date.today)
    my_datetime_field = models.DateTimeField()
    TesterName = models.CharField(max_length=255)

    ALERTNESS_CHOICES = [
        ("0", "0 - Normal (fully alert, but not agitated, throughout assessment)"),
        ("0", "0 - Mild sleepiness for <10 seconds after waking, then normal"),
        ("4", "4 - Clearly abnormal"),
    ]
    AMT4_CHOICES = [
        ("0", "0 - No mistakes"),
        ("1", "1- 1 mistake"),
        ("2", "2 or more mistakes/untestable"),
    ]
    ATTENTION_CHOICES = [
        ("0", "0 - Achieves 7 months or more correctly"),
        ("1", "1 - Starts but scores <7 months / refuses to start"),
        ("2", "2 - Untestable (cannot start because unwell, drowsy, inattentive)"),
    ]
    ACUTE_CHANGE_CHOICES = [
        ("0", "0 - No)"),
        ("4", "4 - Yes"),
    ]

    question1 = models.CharField(max_length=1, choices=ALERTNESS_CHOICES, default="0")
    question2 = models.CharField(max_length=1, choices=AMT4_CHOICES, default="0")
    question3 = models.CharField(max_length=1, choices=ATTENTION_CHOICES, default="0")
    question4 = models.CharField(
        max_length=1, choices=ACUTE_CHANGE_CHOICES, default="0"
    )

    AtScore = models.FloatField()

    # TherapistEmail = forms.EmailField(label='Therapist Email')
    # feature1 = forms.ChoiceField(label="Feature 1: Acute Onset or Fluctuating Course",
    #                              choices=[(Sign.Positive, "Positive"), (Sign.Negative, "Negative")])
    # feature1ExistsInEPIC = forms.ChoiceField(label="Exists in Epic",
    #                                          choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")])
    # feature1Single = forms.CharField()
    # feature2 = forms.ChoiceField(label="Feature 2: Inattention",
    #                              choices=[(Sign.Positive, "Positive"), (Sign.Negative, "Negative")])
    # feature2ExistsInEPIC = forms.ChoiceField(label="Exists in Epic",
    #                                          choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")])
    # feature2Single = forms.CharField()
    # feature3 = forms.ChoiceField(label="Feature 3: Altered Level of Consciousness",
    #                              choices=[(Sign.Positive, "Positive"), (Sign.Negative, "Negative")])
    # feature3ExistsInEPIC = forms.ChoiceField(label="Exists in Epic",
    #                                          choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")])
    # feature3Single = forms.CharField()
    # feature4 = forms.ChoiceField(label="Feature 4: Disorganized Thinking",
    #                              choices=[(Sign.Positive, "Positive"), (Sign.Negative, "Negative")])
    # feature4ExistsInEPIC = forms.ChoiceField(label="Exists in Epic",
    #                                          choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")])
    # feature4Single = forms.CharField()

    def get_info(self):
        form = self
        description = """
            """
        context = {
            "form": form,
            "header": "RasForm/Evaluation",
            "description": description,
        }

        result = render_to_string("email/stomp.html", context)

        logging.info(form.cleaned_data)
        # recipient = form.data['TherapistEmail']
        return "RasForm/Evaluation", result

    def send(self):
        (
            subject,
            msg,
        ) = self.get_info()

        # send_mail(
        #     subject=subject,
        #     message="",
        #     html_message=msg,
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=[recipent]
        # )
