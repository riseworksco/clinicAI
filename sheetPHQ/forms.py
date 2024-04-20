from datetime import date

from django import forms
from django.conf import settings  # Add this import
from django.core.mail import send_mail
from django.template.loader import render_to_string


class PHQForm(forms.Form):
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
            "Not at all", "Several days", "More than half the days", "Nearly every day",
        ], start=0)
    ]


    # 问题字段
    question1 = forms.ChoiceField(
        label='1. Little interest or pleasure in doing things',
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )



    question2 = forms.ChoiceField(
        label='2. Feeling down, depressed, or hopeless',
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )



    question3 = forms.ChoiceField(
        label='3. Trouble falling or staying asleep, or sleeping too much',
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )



    question4 = forms.ChoiceField(
        label='4. Feeling tired or having little energy',
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )



    question5 = forms.ChoiceField(
        label='5. Poor appetite or overeating',
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )



    question6 = forms.ChoiceField(
        label='6. Feeling bad about yourself or that you are a failure or have let yourself or your family down',
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )



    question7 = forms.ChoiceField(
        label='7. Trouble concentrating on things, such as reading the newspaper or watching television',
        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )



    question8 = forms.ChoiceField(
        label='8.Moving or speaking so slowly that other people could have noticed. Or the opposite – being '
                      'so fidgety or restless that you have been moving around a lot more than usual',

        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )




    question9 = forms.ChoiceField(
        label='9. Thoughts that you would be better off dead, or of hurting yourself ',

        choices=QUESTION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )




    question10 = forms.ChoiceField(
        label='10.If you checked off any problems, how difficult have these problems made it for you to do '
                       'your work, take care of things at home, or get along with other people?',
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
        for i in range(1, 9):
            total += int(self.cleaned_data.get(f'question{i}', 0))
        return total

    def get_diagnosis(self, total_score):
        total_score = self.cleaned_data['total_score']
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
