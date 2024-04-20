from datetime import date

from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string


class AAQIIModel(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(default=date.today)

    QUESTION_CHOICES = [
        ('1', "Never true"), 
        ('2', "Very seldom true"), 
        ('3', "Seldom true"),
        ('4', "Sometimes true"), 
        ('5', "Frequently true"), 
        ('6', "Almost always true"),
        ('7', "Always true")
    ]

    question1 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='1')
    question2 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='1')
    question3 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='1')
    question4 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='1')
    question5 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='1')
    question6 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='1')
    question7 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='1')

    def calculate_total_score(self):
        total = 0
        for i in range(1, 8):
            total += int(getattr(self, f'question{i}', '1'))
        return total

    def get_diagnosis(self):
        total_score = self.calculate_total_score()
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
