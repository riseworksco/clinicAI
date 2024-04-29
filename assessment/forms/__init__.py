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
from assessment.models import PsychoemotionalScreeningRecord, stomp_model
from assessment.forms.neurologic_screening_evaluation_form import NeurologicScreeningEvaluationForm
from assessment.forms.StompForm import StompForm

class PrePostForm(forms.Form):
    TherapistEmail = forms.EmailField(label="Therapist Email")
    VITALSExistsInEPIC = forms.ChoiceField(
        label="Exists in Epic", choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")]
    )
    VITALSSingle = forms.CharField()

    BPExistsInEPIC = forms.ChoiceField(
        label="Exists in Epic", choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")]
    )
    BPSingle = forms.CharField()

    BPLocationExistsInEPIC = forms.ChoiceField(
        label="Exists in Epic", choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")]
    )
    BPLocationSingle = forms.CharField()

    PatientPositionExistsInEPIC = forms.ChoiceField(
        label="Exists in Epic", choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")]
    )
    PatientPositionSingle = forms.CharField()

    HRExistsInEPIC = forms.ChoiceField(
        label="Exists in Epic", choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")]
    )
    HRSingle = forms.CharField()

    RRExistsInEPIC = forms.ChoiceField(
        label="Exists in Epic", choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")]
    )
    RRSingle = forms.CharField()
    # O2
    O2ExistsInEPIC = forms.ChoiceField(
        label="Exists in Epic", choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")]
    )
    O2Single = forms.CharField()

    PulseExistsInEPIC = forms.ChoiceField(
        label="Exists in Epic", choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")]
    )
    PulseSingle = forms.CharField()

    PulseOxLocationExistsInEPIC = forms.ChoiceField(
        label="Exists in Epic", choices=[(Sign.Positive, "Yes"), (Sign.Negative, "No")]
    )
    PulseOxLocationSingle = forms.CharField()

    def get_info(self):
        form = self
        description = """
            """
        context = {
            "form": form,
            "header": "PrePostForm",
            "description": description,
        }

        result = render_to_string("email/stomp.html", context)
        logging.info(form.data)
        recipient = form.data["TherapistEmail"]
        return "Pre/Post Tests", result, recipient

    def send(self):
        subject, msg, recipient = self.get_info()

        send_mail(
            subject=subject,
            message="",
            html_message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient],
        )


class PsychoemotionalScreeningEvaluationForm(ModelForm):
    """
    PsychoemotionalScreeningEvaluationForm
    """

    class Meta:
        model = PsychoemotionalScreeningRecord
        fields = ["doctor", "patient"]


class AT4Form(forms.Form):

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


class AAQ2Form(forms.Form):
    # 定义姓名和日期字段
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your name"}
        ),
    )
    date = forms.DateField(
        label="Date",
        initial=date.today,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )

    # 定义问题选项
    QUESTION_CHOICES = [("", "Choose here")] + [
        (str(i), f"{i} - {option}")
        for i, option in enumerate(
            [
                "Never true",
                "Very seldom true",
                "Seldom true",
                "Sometimes true",
                "Frequently true",
                "Almost always true",
                "Always true",
            ],
            start=1,
        )
    ]

    # 为每个问题创建一个选择字段
    question1 = forms.ChoiceField(
        label="1. My painful experiences and memories make it difficult for me to live a life that I would value",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    question2 = forms.ChoiceField(
        label="2. I'm afraid of my feelings",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    question3 = forms.ChoiceField(
        label="3. I worry about not being able to control my worries and feelings",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    question4 = forms.ChoiceField(
        label="4. My painful memories prevent me from having a fulfilling life",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    question5 = forms.ChoiceField(
        label="5. Emotions cause problems in my life",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    question6 = forms.ChoiceField(
        label="6. It seems like most people are handling their lives better than I am",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    question7 = forms.ChoiceField(
        label="7. Worries get in the way of my success",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    def clean(self):
        cleaned_data = super().clean()
        # 这里可以添加自定义验证逻辑
        return cleaned_data

    def calculate_total_score(self):
        total = 0
        for i in range(1, 8):
            total += int(self.cleaned_data.get(f"question{i}", 0))
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
            "form": form,
            "header": "AAQIIForm/Evaluation",
            "description": description,
        }

        result = render_to_string("email/stomp.html", context)

        logging.info(form.data)
        recipient = self.cleaned_data.get(
            "email"
        )  # Replace 'email' with your field name

        return "AAQIIForm/Evaluation", result, recipient

    def send(self):
        subject, msg, recipient = self.get_info()

        send_mail(
            subject=subject,
            message="",
            html_message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient],
        )


class CAM1Form(forms.Form):

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

        logging.info(form.data)
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


class GAD7Form(forms.Form):
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your name"}
        ),
    )
    date = forms.DateField(
        label="Date",
        initial=date.today,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )

    # 问题选项
    QUESTION_CHOICES = [("", "Choose here")] + [
        (str(i), f"{i} - {option}")
        for i, option in enumerate(
            ["Not at all", "Several days", "Over half the days", "Nearly every day"],
            start=0,
        )
    ]

    # 问题字段
    question1 = forms.ChoiceField(
        label="1. Feeling nervous, anxious, or on edge",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    question2 = forms.ChoiceField(
        label="2. Not being able to stop or control worrying",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    question3 = forms.ChoiceField(
        label="3. Worrying too much about different things",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    question4 = forms.ChoiceField(
        label="4. Trouble relaxing",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    question5 = forms.ChoiceField(
        label="5. Being so restless that it is hard to sit still",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    question6 = forms.ChoiceField(
        label="6. Becoming easily annoyed or irritable",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    question7 = forms.ChoiceField(
        label="7. Feeling afraid as if something awful might happen",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    question8 = forms.ChoiceField(
        label="8. If you checked off any problems, how difficult have these made it for you to do your work, "
        "take care of things at home, or get along with other people?",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    # 可以添加自定义验证方法或其他方法
    def clean(self):
        cleaned_data = super().clean()
        # 这里可以添加自定义验证逻辑
        return cleaned_data

    def calculate_total_score(self):
        total = 0
        for i in range(1, 8):
            total += int(self.cleaned_data.get(f"question{i}", 0))
        return total

    def get_anxiety_level(self, total_score):
        # 根据总分判断诊断
        if total_score < 5:
            return "Minimal anxiety or none at all."
        elif total_score < 10:
            return "Mild anxiety."
        elif total_score < 15:
            return "Moderate anxiety."
        else:
            return "Severe anxiety."

    def get_info(self):
        form = self
        description = """
            """
        context = {
            "form": form,
            "header": "GAD7Form/Evaluation",
            "description": description,
        }

        result = render_to_string("email/stomp.html", context)

        logging.info(form.data)
        recipient = self.cleaned_data.get(
            "email"
        )  # Replace 'email' with your field name

        return "GAD7Form/Evaluation", result, recipient

    def send(self):
        subject, msg, recipient = self.get_info()

        send_mail(
            subject=subject,
            message="",
            html_message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient],
        )


class PHQ9Form(forms.Form):
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your name"}
        ),
    )
    date = forms.DateField(
        label="Date",
        initial=date.today,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )

    # 问题选项
    QUESTION_CHOICES = [("", "Choose here")] + [
        (str(i), f"{i} - {option}")
        for i, option in enumerate(
            [
                "Not at all",
                "Several days",
                "More than half the days",
                "Nearly every day",
            ],
            start=0,
        )
    ]

    # 问题字段
    question1 = forms.ChoiceField(
        label="1. Little interest or pleasure in doing things",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    question2 = forms.ChoiceField(
        label="2. Feeling down, depressed, or hopeless",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    question3 = forms.ChoiceField(
        label="3. Trouble falling or staying asleep, or sleeping too much",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    question4 = forms.ChoiceField(
        label="4. Feeling tired or having little energy",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    question5 = forms.ChoiceField(
        label="5. Poor appetite or overeating",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    question6 = forms.ChoiceField(
        label="6. Feeling bad about yourself or that you are a failure or have let yourself or your family down",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    question7 = forms.ChoiceField(
        label="7. Trouble concentrating on things, such as reading the newspaper or watching television",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    question8 = forms.ChoiceField(
        label="8.Moving or speaking so slowly that other people could have noticed. Or the opposite – being "
        "so fidgety or restless that you have been moving around a lot more than usual",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    question9 = forms.ChoiceField(
        label="9. Thoughts that you would be better off dead, or of hurting yourself ",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    question10 = forms.ChoiceField(
        label="10.If you checked off any problems, how difficult have these problems made it for you to do "
        "your work, take care of things at home, or get along with other people?",
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    # 可以添加自定义验证方法或其他方法
    def clean(self):
        cleaned_data = super().clean()
        # 这里可以添加自定义验证逻辑
        return cleaned_data

    def calculate_total_score(self):
        total = 0
        for i in range(1, 10):
            total += int(self.cleaned_data.get(f"question{i}", 0))
        return total

    def get_diagnosis(self, total_score):  # 注意这里我们将total_score作为参数传递
        if total_score <= 4:
            return "Minimal depression"
        elif total_score <= 9:
            return "Mild depression"
        elif total_score <= 14:
            return "Moderate depression"
        elif total_score <= 19:
            return "Moderately severe depression"
        else:
            return "Severe depression"

    def get_info(self):
        form = self
        total_score = self.calculate_total_score()  # 计算总分
        diagnosis = self.get_diagnosis(total_score)  # 使用总分调用get_diagnosis

        description = f"Diagnosis: {diagnosis}"
        context = {
            "form": form,
            "header": "PHQForm/Evaluation",
            "description": description,
        }

        result = render_to_string("email/stomp.html", context)

        logging.info(form.cleaned_data)
        recipient = self.cleaned_data.get("email")

        return "PHQForm/Evaluation", result, recipient

    def send(self):
        subject, msg, recipient = self.get_info()

        send_mail(
            subject=subject,
            message="",
            html_message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient],
        )


class RASForm(forms.Form):

    patientName = forms.CharField(
        widget=forms.TextInput(attrs={"class": "emailinput form-control"})
    )
    initialWalk = forms.FloatField(
        min_value=0,
        widget=forms.TextInput(attrs={"class": "emailinput form-control"}),
    )

    firstWalkSteps = forms.FloatField(
        label="Steps",
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Enter stesps",
                "oninput": "performDivision()",
            }
        ),
    )
    firstWalkSeconds = forms.FloatField(
        label="Seconds",
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Enter seconds",
                "oninput": "performDivision()",
            }
        ),
    )
    firstCadence = forms.FloatField(
        label="First Cadence",
    )
    firstVelocity = forms.FloatField(label="First Velocity")
    firstStrideLength = forms.FloatField(
        label="First Stride Length",
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

        logging.info(form.data)
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
