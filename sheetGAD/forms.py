from datetime import date

from django import forms
from django.conf import settings  # Add this import
from django.core.mail import send_mail
from django.template.loader import render_to_string


class GAD7Form(forms.Form):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'})
    )
    date = forms.DateField(
        label='Date',
        initial=date.today,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )

    # 问题选项
    QUESTION_CHOICES = [('', 'Choose here')] + [
        (str(i), f"{i} - {option}") for i, option in enumerate([
            "Not at all", "Several days", "Over half the days", "Nearly every day"
        ], start=0)
    ]

    # 问题字段
    question1 = forms.ChoiceField(
        label='1. Feeling nervous, anxious, or on edge',
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    question2 = forms.ChoiceField(
        label='2. Not being able to stop or control worrying',
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    question3 = forms.ChoiceField(
        label='3. Worrying too much about different things',
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    question4 = forms.ChoiceField(
        label='4. Trouble relaxing',
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    question5 = forms.ChoiceField(
        label='5. Being so restless that it is hard to sit still',
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    question6 = forms.ChoiceField(
        label='6. Becoming easily annoyed or irritable',
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    question7 = forms.ChoiceField(
        label='7. Feeling afraid as if something awful might happen',
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    question8 = forms.ChoiceField(
        label='8. If you checked off any problems, how difficult have these made it for you to do your work, '
              'take care of things at home, or get along with other people?',
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # 可以添加自定义验证方法或其他方法
    def clean(self):
        cleaned_data = super().clean()
        # 这里可以添加自定义验证逻辑
        return cleaned_data

    def calculate_total_score(self):
        total = 0
        for i in range(1, 8):
            total += int(self.cleaned_data.get(f'question{i}', 0))
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
            'form': form,
            'header': 'GAD7Form/Evaluation',
            'description': description, }

        result = render_to_string('email/stomp.html', context)

        print(form.data)
        recipient = self.cleaned_data.get('email')  # Replace 'email' with your field name

        return 'GAD7Form/Evaluation', result, recipient

    def send(self):
        subject, msg, recipient = self.get_info()

        send_mail(
            subject=subject,
            message="",
            html_message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient]
        )
