from django.db import models
from datetime import date
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

class PHQModel(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(default=date.today)

    QUESTION_CHOICES = [
        ('0', "Not at all"),
        ('1', "Several days"),
        ('2', "More than half the days"),
        ('3', "Nearly every day")
    ]

    question1 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='0')
    question2 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='0')
    question3 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='0')
    question4 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='0')
    question5 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='0')
    question6 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='0')
    question7 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='0')
    question8 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='0')
    question9 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='0')
    question10 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='0')

    def save(self, *args, **kwargs):
        # Custom validation logic before saving (if needed)
        self.full_clean()  # Calls the model's clean method
        super().save(*args, **kwargs)  # Don't forget to call the superclass method!

    def clean(self):
        # Example validation: ensure 'name' field is not empty
        if not self.name:
            raise ValidationError({'name': "Name cannot be empty."})
        # Add more validation as needed

    def calculate_total_score(self):
        total = 0
        # Adjust the range according to the actual number of questions
        for i in range(1, 11):  # Assuming there are 10 questions
            total += int(getattr(self, f'question{i}', '0'))
        return total

    def get_diagnosis(self):
        total_score = self.calculate_total_score()
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
        description = """
            """
        context = {
            'form': form,
            'header': 'PHQForm/Evaluation',
            'description': description, }

        result = render_to_string('email/stomp.html', context)

        print(form.data)
        recipient = self.cleaned_data.get('email')  # Replace 'email' with your field name

        return 'PHQForm/Evaluation', result, recipient

    def send(self):
        subject, msg, recipient = self.get_info()

        send_mail(
            subject=subject,
            message="",
            html_message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient]
        )

