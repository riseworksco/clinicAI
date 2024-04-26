import logging

from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.forms import ModelForm
from django.template.loader import render_to_string

from assessment.identifiers import Sign


class ATForm(forms.Form):

    patientName = forms.CharField(
        widget=forms.TextInput(attrs={"class": "emailinput form-control"})
    )
    patientNumber = forms.CharField(
        widget=forms.TextInput(attrs={"class": "emailinput form-control"})
    )
    birthDate = forms.DateField(
        label="Choose a date",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        input_formats=["%Y-%m-%d"],  # Specify the input format if needed
    )

    my_datetime_field = forms.DateTimeField(
        label="Choose a date and time",
        widget=forms.DateTimeInput(
            attrs={"class": "form-control", "type": "datetime-local"}
        ),
        input_formats=["%Y-%m-%dT%H:%M"],  # Specify the input format if needed
    )

    TesterName = forms.CharField(
        widget=forms.TextInput(attrs={"class": "emailinput form-control"})
    )

    question1 = forms.ChoiceField(
        label="1. ALERTNESS",
        choices=[
            ("0", "0 - Normal (fully alert, but not agitated, throughout assessment)"),
            ("0", "0 - Mild sleepiness for <10 seconds after waking, then normal	"),
            ("4", "4 - Clearly abnormal"),
        ],
        widget=forms.Select(
            attrs={
                "oninput": "performDivision()",
            }
        ),
    )
    question2 = forms.ChoiceField(
        label="2. AMT4",
        choices=[
            ("0", "0 - No mistakes"),
            ("1", "1- 1 mistake	"),
            ("2", "2 or more mistakes/untestable	"),
        ],
        widget=forms.Select(
            attrs={
                "oninput": "performDivision()",
            }
        ),
    )
    question3 = forms.ChoiceField(
        label="3. ATTENTION——Months of the year backwards",
        choices=[
            ("0", "0 - Achieves 7 months or more correctly"),
            ("1", "1 - Starts but scores <7 months / refuses to start"),
            ("2", "2 - Untestable (cannot start because unwell, drowsy, inattentive)	"),
        ],
        widget=forms.Select(
            attrs={
                "oninput": "performDivision()",
            }
        ),
    )
    question4 = forms.ChoiceField(
        label="4. ACUTE CHANGE OR FLUCTUATING COURSE",
        choices=[("0", "0 - No)"), ("4", "4 - Yes")],
        widget=forms.Select(
            attrs={
                "oninput": "performDivision()",
            }
        ),
    )

    AtScore = forms.FloatField(
        label="4AT SCORE",
    )

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
