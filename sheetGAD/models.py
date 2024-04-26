from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string


class GAD7Submission(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)

    QUESTION_CHOICES = [
        (0, "Not at all"),
        (1, "Several days"),
        (2, "Over half the days"),
        (3, "Nearly every day"),
    ]

    question1 = models.IntegerField(choices=QUESTION_CHOICES, default=0)
    question2 = models.IntegerField(choices=QUESTION_CHOICES, default=0)
    question3 = models.IntegerField(choices=QUESTION_CHOICES, default=0)
    question4 = models.IntegerField(choices=QUESTION_CHOICES, default=0)
    question5 = models.IntegerField(choices=QUESTION_CHOICES, default=0)
    question6 = models.IntegerField(choices=QUESTION_CHOICES, default=0)
    question7 = models.IntegerField(choices=QUESTION_CHOICES, default=0)
    question8 = models.IntegerField(choices=QUESTION_CHOICES, default=0)
    email = (
        models.EmailField()
    )  # Assuming you're collecting emails. Add this field if necessary.

    def calculate_total_score(self):
        total = sum([getattr(self, f"question{i}") for i in range(1, 8)])
        return total

    def get_anxiety_level(self):
        total_score = self.calculate_total_score()
        if total_score < 5:
            return "Minimal anxiety or none at all."
        elif total_score < 10:
            return "Mild anxiety."
        elif total_score < 15:
            return "Moderate anxiety."
        else:
            return "Severe anxiety."

    def get_info(self):
        description = """
            Your anxiety level has been evaluated.
        """
        context = {
            "name": self.name,
            "date": self.date,
            "total_score": self.calculate_total_score(),
            "anxiety_level": self.get_anxiety_level(),
            "description": description,
        }

        result = render_to_string(
            "email/template.html", context
        )  # Ensure this template exists
        recipient = (
            self.email
        )  # Ensure you have a field to capture the recipient's email
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
