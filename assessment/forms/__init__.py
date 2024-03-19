from django import forms
from django.conf import settings
from django.forms import ModelForm
from django.template.loader import render_to_string
from django.http import FileResponse
from django.core.mail import EmailMessage
from reportlab.pdfgen import canvas

from assessment.identifiers import Sign
from django.core.mail import send_mail

from assessment.models import PsychoemotionalScreeningRecord, ATNModel

from django import forms
from django.conf import settings
from django.forms import ModelForm
from django.template.loader import render_to_string

from assessment.identifiers import Sign
from django.core.mail import send_mail
from datetime import date


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
        recipient = form.data['TherapistEmail']
        return 'STOMP-Revised', result, recipient

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
        response = FileResponse(self.generate_pdf_file(),
                                as_attachment=True,
                                filename='music_preference_form.pdf')
        return response


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

        send_mail(
            subject=subject,
            message="",
            html_message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipent]
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

        send_mail(
            subject=subject,
            message="",
            html_message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient]
        )


class PsychoemotionalScreeningEvaluationForm(ModelForm):
    """
    PsychoemotionalScreeningEvaluationForm
    """

    class Meta:
        model = PsychoemotionalScreeningRecord
        fields = ['doctor', 'patient']








class ATNForm(forms.Form):

    patientName = forms.CharField(widget=forms.TextInput(attrs={'class': 'emailinput form-control'}))
    patientNumber = forms.CharField(widget=forms.TextInput(attrs={'class': 'emailinput form-control'}))
    birthDate = forms.DateField(
        label='Choose a date',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        input_formats=['%Y-%m-%d'],  # Specify the input format if needed
    )

    my_datetime_field = forms.DateTimeField(
        label='Choose a date and time',
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],  # Specify the input format if needed
    )

    TesterName = forms.CharField(widget=forms.TextInput(attrs={'class': 'emailinput form-control'}))

    question1 = forms.ChoiceField(label='1. ALERTNESS',
                                  choices=[('0', '0 - Normal (fully alert, but not agitated, throughout assessment)'),
                                           ('0', '0 - Mild sleepiness for <10 seconds after waking, then normal	'),
                                           ('4', '4 - Clearly abnormal')],
                                  widget=forms.Select(attrs={

                                      'oninput': 'performDivision()',
                                  })
                                  )
    question2 = forms.ChoiceField(label='2. AMT4',
                                  choices=[('0', '0 - No mistakes'),
                                           ('1', '1- 1 mistake	'),
                                           ('2', '2 or more mistakes/untestable	')],
                                  widget=forms.Select(attrs={

                                      'oninput': 'performDivision()',
                                  })
                                  )
    question3 = forms.ChoiceField(label='3. ATTENTION——Months of the year backwards',
                                  choices=[('0', '0 - Achieves 7 months or more correctly'),
                                           ('1', '1 - Starts but scores <7 months / refuses to start'),
                                           ('2', '2 - Untestable (cannot start because unwell, drowsy, inattentive)	')],
                                  widget=forms.Select(attrs={

                                      'oninput': 'performDivision()',
                                  })
                                  )
    question4 = forms.ChoiceField(label='4. ACUTE CHANGE OR FLUCTUATING COURSE',
                                  choices=[('0', '0 - No)'),
                                           ('4', '4 - Yes')],
                                  widget=forms.Select(attrs={

                                      'oninput': 'performDivision()',
                                  })
                                  )

    AtScore = forms.FloatField(label='4AT SCORE', )


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
            'form': form,
            'header': 'ATNForm',
            'description': description, }

        result = render_to_string('email/stomp.html', context)

        print(form.cleaned_data)
        # recipient = form.data['TherapistEmail']
        return 'ATNForm', result

    def send(self):
        subject, msg, = self.get_info()

        # send_mail(
        #     subject=subject,
        #     message="",
        #     html_message=msg,
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=[recipent]
        # )



class AAQ2Form(forms.Form):
    # 定义姓名和日期字段
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'})
    )
    date = forms.DateField(
        label='Date',
        initial=date.today,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )

    # 定义问题选项
    QUESTION_CHOICES = [('','Choose here')] + [
        (str(i), f"{i} - {option}") for i, option in enumerate([
            "Never true", "Very seldom true", "Seldom true",
            "Sometimes true", "Frequently true", "Almost always true",
            "Always true"
        ], start=1)
    ]

    # 为每个问题创建一个选择字段
    question1 = forms.ChoiceField(
        label='1. My painful experiences and memories make it difficult for me to live a life that I would value',
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    question2 = forms.ChoiceField(
        label="2. I'm afraid of my feelings",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    question3 = forms.ChoiceField(
        label="3. I worry about not being able to control my worries and feelings",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    question4 = forms.ChoiceField(
        label="4. My painful memories prevent me from having a fulfilling life",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    question5 = forms.ChoiceField(
        label="5. Emotions cause problems in my life",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    question6 = forms.ChoiceField(
        label="6. It seems like most people are handling their lives better than I am",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    question7 = forms.ChoiceField(
        label="7. Worries get in the way of my success",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        # 这里可以添加自定义验证逻辑
        return cleaned_data

    def calculate_total_score(self):
        total = 0
        for i in range(1, 8):
            total += int(self.cleaned_data.get(f'question{i}', 0))
        return total

    def get_diagnosis(self, total_score):
        if total_score > 24 and total_score <= 28:
            return "Probable current clinical distress, future distress & work absence more likely."
        elif total_score > 28:
            return "High likelihood of clinical distress."
        else:
            return "Likely non-clinical level of distress."


    def get_info(self):
        form = self
        description = """
            """
        context = {
            'form': form,
            'header': 'AAQIIForm/Evaluation',
            'description': description, }

        result = render_to_string('email/stomp.html', context)

        print(form.data)
        recipient = self.cleaned_data.get('email')  # Replace 'email' with your field name

        return 'AAQIIForm/Evaluation', result, recipient

    def send(self):
        subject, msg, recipient = self.get_info()

        send_mail(
            subject=subject,
            message="",
            html_message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient]
        )
