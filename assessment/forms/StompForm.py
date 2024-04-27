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


class StompForm(forms.Form):
    """
    Music Preference Form
    """

    TherapistEmail = forms.EmailField(label="Therapist Email")
    Alternative = forms.IntegerField(label="Alternative", min_value=1, max_value=5)
    Bluegrass = forms.IntegerField(label="Bluegrass", min_value=1, max_value=5)
    Blues = forms.IntegerField(label="Blues", min_value=1, max_value=5)
    Classical = forms.IntegerField(label="Classical", min_value=1, max_value=5)
    Country = forms.IntegerField(label="Country", min_value=1, max_value=5)
    Dance_Electronica = forms.IntegerField(
        label="Dance/Electronica", min_value=1, max_value=5
    )
    Folk = forms.IntegerField(label="Folk", min_value=1, max_value=5)
    Funk = forms.IntegerField(label="Funk", min_value=1, max_value=5)
    Gospel = forms.IntegerField(label="Gospel", min_value=1, max_value=5)
    Heavy_Meta = forms.IntegerField(label=" Heavy Meta", min_value=1, max_value=5)
    World = forms.IntegerField(label="World", min_value=1, max_value=5)
    Jazz = forms.IntegerField(label="Jazz", min_value=1, max_value=5)
    New_Age = forms.IntegerField(label="New_Age", min_value=1, max_value=5)
    Oldies = forms.IntegerField(label="Oldies", min_value=1, max_value=5)
    Opera = forms.IntegerField(label="Opera", min_value=1, max_value=5)
    Pop = forms.IntegerField(label="Pop", min_value=1, max_value=7)
    Punk = forms.IntegerField(label="Punk", min_value=1, max_value=7)
    Rap_hip_hop = forms.IntegerField(label="Rap/hip-hop", min_value=1, max_value=7)
    Reggae = forms.IntegerField(label="Reggae", min_value=1, max_value=7)
    Religious = forms.IntegerField(label="Religious", min_value=1, max_value=7)
    Rock = forms.IntegerField(label="Rock", min_value=1, max_value=7)
    Soul_R_B = forms.IntegerField(label=" Soul/R&B", min_value=1, max_value=7)
    Soundtracks_heme_song = forms.IntegerField(
        label="Soundtracks/theme song", min_value=1, max_value=7
    )

    def get_info(self):
        form = self
        description = """
                Please indicate your basic preference for each of the following genres using the scale provided.
        1-----------------2-----------------3-----------------4-----------------5-----------------6-----------------7
        Dislike Dislike Dislike a Neither like Like a Like Like
            """
        context = {
            "form": form,
            "header": "STOMP-Revised",
            "description": description,
        }

        result = render_to_string("email/stomp.html", context)
        recipient = form.data["TherapistEmail"]
        return "STOMP-Revised", result, recipient

    def send(self):
        subject, msg, recipent = self.get_info()
        pdf = self.generate_pdf_file().getbuffer()
        email = EmailMessage(
            subject=subject,
            from_email=settings.EMAIL_HOST_USER,
            to=[recipent],
        )
        email.attach("music_preferences.pdf", pdf, "application/pdf")
        email.send()

    def generate_pdf_file(self):
        from io import BytesIO

        buffer = BytesIO()
        p = canvas.Canvas(buffer)

        # Create a PDF document
        p.drawString(100, 750, "Music Preference Form")

        x = 100
        y = 700
        for key in self.data.keys():
            if key != "csrfmiddlewaretoken":
                p.drawString(100, y, f"{key}: {str(self.data[key])}")
                y -= 20

        p.showPage()
        p.save()

        buffer.seek(0)
        return buffer

    def generate_pdf(self):
        response = FileResponse(
            self.generate_pdf_file(),
            as_attachment=True,
            filename="music_preference_form.pdf",
        )
        return response
