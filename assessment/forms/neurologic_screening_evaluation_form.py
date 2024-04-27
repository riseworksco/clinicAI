# Copyright 2024 Yuan Chen
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from datetime import date

from django import forms
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.forms import ModelForm
from django.http import FileResponse
from django.template.loader import render_to_string
from reportlab.pdfgen import canvas

from assessment.identifiers import Sign
from assessment.models import PsychoemotionalScreeningRecord



class NeurologicScreeningEvaluationForm(forms.Form):
    TherapistEmail = forms.EmailField(label="Therapist Email")
    feature1 = forms.ChoiceField(
        label="Feature 1: Acute Onset or Fluctuating Course",
        choices=[(Sign.Positive, "Positive"), (Sign.Negative, "Negative")],
    )
    feature1ExistsInEPIC = forms.ChoiceField(
        label="Exists in Epic", choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")]
    )
    feature1Single = forms.CharField()
    feature2 = forms.ChoiceField(
        label="Feature 2: Inattention",
        choices=[(Sign.Positive, "Positive"), (Sign.Negative, "Negative")],
    )
    feature2ExistsInEPIC = forms.ChoiceField(
        label="Exists in Epic", choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")]
    )
    feature2Single = forms.CharField()
    feature3 = forms.ChoiceField(
        label="Feature 3: Altered Level of Consciousness",
        choices=[(Sign.Positive, "Positive"), (Sign.Negative, "Negative")],
    )
    feature3ExistsInEPIC = forms.ChoiceField(
        label="Exists in Epic", choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")]
    )
    feature3Single = forms.CharField()
    feature4 = forms.ChoiceField(
        label="Feature 4: Disorganized Thinking",
        choices=[(Sign.Positive, "Positive"), (Sign.Negative, "Negative")],
    )
    feature4ExistsInEPIC = forms.ChoiceField(
        label="Exists in Epic", choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")]
    )
    feature4Single = forms.CharField()

    def get_info(self):
        form = self
        description = """
            """
        context = {
            "form": form,
            "header": "Neurologic Screening/Evaluation",
            "description": description,
        }

        result = render_to_string("email/stomp.html", context)
        logging.info(form.data)
        recipient = form.data["TherapistEmail"]
        return "Neurologic Screening/Evaluation", result, recipient

    def send(self):
        subject, msg, recipent = self.get_info()

        send_mail(
            subject=subject,
            message="",
            html_message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipent],
        )