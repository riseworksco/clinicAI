from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.forms import ModelForm
from django.template.loader import render_to_string

from assessment.identifiers import Sign


class CAMForm(forms.Form):

    patientName = forms.CharField(
        widget=forms.TextInput(attrs={"class": "emailinput form-control"})
    )

    my_datetime_field = forms.DateTimeField(
        label="Choose a date and time",
        widget=forms.DateTimeInput(
            attrs={"class": "form-control", "type": "datetime-local"}
        ),
        input_formats=["%Y-%m-%dT%H:%M"],  # Specify the input format if needed
    )

    checkbox1 = forms.BooleanField(
        label="Click me",
        required=False,  # Set to True if the checkbox must be checked
        widget=forms.CheckboxInput(
            attrs={"class": "custom-checkbox", "onclick": "performDivision();"}
        ),
    )

    checkbox2 = forms.BooleanField(
        label="Click me",
        required=False,  # Set to True if the checkbox must be checked
        widget=forms.CheckboxInput(
            attrs={"class": "custom-checkbox", "onclick": "performDivision();"}
        ),
    )
    checkbox3 = forms.BooleanField(
        label="Click me",
        required=False,  # Set to True if the checkbox must be checked
        widget=forms.CheckboxInput(
            attrs={"class": "custom-checkbox", "onclick": "performDivision();"}
        ),
    )
    checkbox4 = forms.BooleanField(
        label="Click me",
        required=False,  # Set to True if the checkbox must be checked
        widget=forms.CheckboxInput(
            attrs={"class": "custom-checkbox", "onclick": "performDivision();"}
        ),
    )

    checkbox5 = forms.BooleanField(
        label="CAM-ICU POSITIVE",
        required=False,  # Set to True if the checkbox must be checked
        widget=forms.CheckboxInput(attrs={"class": "custom-checkbox"}),
    )
    checkbox6 = forms.BooleanField(
        label="CAM-ICU NEGATIVE",
        required=False,  # Set to True if the checkbox must be checked
        widget=forms.CheckboxInput(attrs={"class": "custom-checkbox"}),
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

        print(form.data)
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
