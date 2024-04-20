import logging
from datetime import date

from django import forms
from django.conf import settings  # Add this import
from django.core.mail import send_mail
from django.template.loader import render_to_string


class AAQIIForm(forms.Form):
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

        logging.info(form.data)
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