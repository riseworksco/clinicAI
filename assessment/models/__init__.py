from django.db import models

from patient_management.models import Doctor, Patient
import datetime
from datetime import date
from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings



# Create your models here.
class Stomp(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    Alternative = models.IntegerField()
    Bluegrass = models.IntegerField()
    Blues = models.IntegerField()
    Classical = models.IntegerField()
    Country = models.IntegerField()
    Dance_Electronica = models.IntegerField()
    Folk = models.IntegerField()
    Funk = models.IntegerField()
    Gospel = models.IntegerField()
    Heavy_Meta = models.IntegerField()
    World = models.IntegerField()


# PsychoemotionalScreeningRecord stuffs
class GAD2(models.Model):
    # 1. Feeling nervous, anxious on edge
    q1_value = models.IntegerField()
    q1_epic = models.CharField('No', max_length=30)
    q1_smf = models.IntegerField()

    q2_value = models.IntegerField()
    q2_epic = models.IntegerField()
    q2_smf = models.IntegerField()

    # Score
    score = models.IntegerField()  # Total Number
    score_epic = models.CharField('No', max_length=30)
    score_smf = models.CharField('FR', max_length=30)

    # Interpretation
    interpretation = models.TextField()
    interpretation_epic = models.CharField('No', max_length=30)
    interpretation_smf = models.CharField('FR', max_length=30)


class GAD7(models.Model):
    q1_value = models.IntegerField()
    q1_epic = models.CharField('No', max_length=30)
    q1_smf = models.IntegerField()

    q2_value = models.IntegerField()
    q2_epic = models.IntegerField()
    q2_smf = models.IntegerField()

    q3_value = models.IntegerField()
    q3_epic = models.CharField('No', max_length=30)
    q3_smf = models.IntegerField()

    q4_value = models.IntegerField()
    q4_epic = models.IntegerField()
    q4_smf = models.IntegerField()

    q5_value = models.IntegerField()
    q5_epic = models.CharField('No', max_length=30)
    q5_smf = models.IntegerField()

    q6_value = models.IntegerField()
    q6_epic = models.IntegerField()
    q6_smf = models.IntegerField()

    q7_value = models.IntegerField()
    q7_epic = models.IntegerField()
    q7_smf = models.IntegerField()

    # Score
    score = models.IntegerField()  # Total Number
    score_epic = models.CharField('No', max_length=30)
    score_smf = models.CharField('FR', max_length=30)

    # Interpretation
    interpretation = models.TextField()
    interpretation_epic = models.CharField('No', max_length=30)
    interpretation_smf = models.CharField('FR', max_length=30)


class PHQ2(models.Model):
    # 1. Feeling nervous, anxious on edge
    q1_value = models.IntegerField()
    q1_epic = models.CharField('No', max_length=30)
    q1_smf = models.CharField('No', max_length=30)

    q2_value = models.IntegerField()
    q2_epic = models.IntegerField()
    q2_smf = models.IntegerField()

    # Score
    score = models.IntegerField()  # Total Number
    score_epic = models.CharField('No', max_length=30)
    score_smf = models.CharField('FR', max_length=30)

    # Interpretation
    interpretation = models.TextField()
    interpretation_epic = models.CharField('No', max_length=30)
    interpretation_smf = models.CharField('FR', max_length=30)


class PHQ9(models.Model):
    q1_value = models.IntegerField()
    q1_epic = models.CharField('No', max_length=30)
    q1_smf = models.IntegerField()

    q2_value = models.IntegerField()
    q2_epic = models.IntegerField()
    q2_smf = models.IntegerField()

    q3_value = models.IntegerField()
    q3_epic = models.CharField('No', max_length=30)
    q3_smf = models.IntegerField()

    q4_value = models.IntegerField()
    q4_epic = models.IntegerField()
    q4_smf = models.IntegerField()

    q5_value = models.IntegerField()
    q5_epic = models.CharField('No''No', max_length=30)
    q5_smf = models.IntegerField()

    q6_value = models.IntegerField()
    q6_epic = models.IntegerField()
    q6_smf = models.IntegerField()

    q7_value = models.IntegerField()
    q7_epic = models.IntegerField()
    q7_smf = models.IntegerField()

    # Score
    score = models.IntegerField()  # Total Number
    score_epic = models.CharField('No', max_length=30)
    score_smf = models.CharField('FR', max_length=30)

    # Interpretation
    interpretation = models.TextField()
    interpretation_epic = models.CharField('No', max_length=30)
    interpretation_smf = models.CharField('FR', max_length=30)


class PsychoemotionalScreeningRecord(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    GAD2 = models.OneToOneField(GAD2, on_delete=models.CASCADE, )
    GAD7 = models.OneToOneField(GAD7, on_delete=models.CASCADE, )
    PHQ2 = models.OneToOneField(PHQ2, on_delete=models.CASCADE, )
    PHQ9 = models.OneToOneField(PHQ9, on_delete=models.CASCADE, )


class CatCatFlowsheetRecord(models.Model):
    """
    CatCatFlowsheetRecord
    """
    type1_value = models.CharField('eval', max_length=30)
    type1_epic = models.CharField('No', max_length=30)
    type1_smf = models.IntegerField()

    type2_value = models.CharField('treatment', max_length=30)
    type2_epic = models.CharField('No', max_length=30)
    type2_smf = models.IntegerField()

    type3_value = models.CharField('treatment pre', max_length=30)
    type3_epic = models.CharField('No', max_length=30)
    type3_smf = models.IntegerField()

    type4_value = models.CharField('treatment post', max_length=30)
    type4_epic = models.CharField('No', max_length=30)
    type4_smf = models.IntegerField()


class AT4Model(models.Model):
    patientName = models.CharField(max_length=255)
    patientNumber = models.CharField(max_length=255)
    birthDate = models.DateField(default=datetime.date.today)
    my_datetime_field = models.DateTimeField()
    TesterName = models.CharField(max_length=255)

    ALERTNESS_CHOICES = [
        ('0', '0 - Normal (fully alert, but not agitated, throughout assessment)'),
        ('0', '0 - Mild sleepiness for <10 seconds after waking, then normal'),
        ('4', '4 - Clearly abnormal'),
    ]
    AMT4_CHOICES = [
        ('0', '0 - No mistakes'),
        ('1', '1- 1 mistake'),
        ('2', '2 or more mistakes/untestable'),
    ]
    ATTENTION_CHOICES = [
        ('0', '0 - Achieves 7 months or more correctly'),
        ('1', '1 - Starts but scores <7 months / refuses to start'),
        ('2', '2 - Untestable (cannot start because unwell, drowsy, inattentive)'),
    ]
    ACUTE_CHANGE_CHOICES = [
        ('0', '0 - No)'),
        ('4', '4 - Yes'),
    ]

    question1 = models.CharField(max_length=1, choices=ALERTNESS_CHOICES, default='0')
    question2 = models.CharField(max_length=1, choices=AMT4_CHOICES, default='0')
    question3 = models.CharField(max_length=1, choices=ATTENTION_CHOICES, default='0')
    question4 = models.CharField(max_length=1, choices=ACUTE_CHANGE_CHOICES, default='0')

    AtScore = models.FloatField()

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
            'header': 'RasForm/Evaluation',
            'description': description, }

        result = render_to_string('email/stomp.html', context)

        print(form.cleaned_data)
        # recipient = form.data['TherapistEmail']
        return 'RasForm/Evaluation', result

    def send(self):
        subject, msg, = self.get_info()

        # send_mail(
        #     subject=subject,
        #     message="",
        #     html_message=msg,
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=[recipent]
        # )


class AAQ2Model(models.Model):
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


class CAM1Model(models.Model):
    patientName = models.CharField(max_length=255)
    my_datetime_field = models.DateTimeField()
    checkbox1 = models.BooleanField(default=False)
    checkbox2 = models.BooleanField(default=False)
    checkbox3 = models.BooleanField(default=False)
    checkbox4 = models.BooleanField(default=False)
    checkbox5 = models.BooleanField(default=False, verbose_name='CAM-ICU POSITIVE')
    checkbox6 = models.BooleanField(default=False, verbose_name='CAM-ICU NEGATIVE')

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
            'header': 'RasForm/Evaluation',
            'description': description, }

        result = render_to_string('email/stomp.html', context)

        print(form.data)
        # recipient = form.data['TherapistEmail']
        return 'RasForm/Evaluation', result

    def send(self):
        subject, msg, = self.get_info()

        # send_mail(
        #     subject=subject,
        #     message="",
        #     html_message=msg,
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=[recipent]
        # )




class GAD7Model(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)

    QUESTION_CHOICES = [
        (0, "Not at all"),
        (1, "Several days"),
        (2, "Over half the days"),
        (3, "Nearly every day")
    ]

    question1 = models.IntegerField(choices=QUESTION_CHOICES, default=0)
    question2 = models.IntegerField(choices=QUESTION_CHOICES, default=0)
    question3 = models.IntegerField(choices=QUESTION_CHOICES, default=0)
    question4 = models.IntegerField(choices=QUESTION_CHOICES, default=0)
    question5 = models.IntegerField(choices=QUESTION_CHOICES, default=0)
    question6 = models.IntegerField(choices=QUESTION_CHOICES, default=0)
    question7 = models.IntegerField(choices=QUESTION_CHOICES, default=0)
    question8 = models.IntegerField(choices=QUESTION_CHOICES, default=0)
    email = models.EmailField()  # Assuming you're collecting emails. Add this field if necessary.

    def calculate_total_score(self):
        total = sum([
            getattr(self, f'question{i}') for i in range(1, 8)
        ])
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
            'name': self.name,
            'date': self.date,
            'total_score': self.calculate_total_score(),
            'anxiety_level': self.get_anxiety_level(),
            'description': description,
        }

        result = render_to_string('email/template.html', context)  # Ensure this template exists
        recipient = self.email  # Ensure you have a field to capture the recipient's email
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




class PHQ9Model(models.Model):
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
        cleaned_data = super().clean()

        return cleaned_data

    def calculate_total_score(self):
        total = 0
        for i in range(1, 10):
            total += int(self.cleaned_data.get(f'question{i}', 0))
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





class RASModel(models.Model):
    patientName = models.CharField(max_length=255)
    initialWalk = models.FloatField()
    firstWalkSteps = models.FloatField()
    firstWalkSeconds = models.FloatField()
    firstCadence = models.FloatField()
    firstVelocity = models.FloatField()
    firstStrideLength = models.FloatField()

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
            'header': 'RasForm/Evaluation',
            'description': description, }

        result = render_to_string('email/stomp.html', context)

        print(form.data)
        # recipient = form.data['TherapistEmail']
        return 'RasForm/Evaluation', result

    def send(self):
        subject, msg, = self.get_info()

        # send_mail(
        #     subject=subject,
        #     message="",
        #     html_message=msg,
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=[recipent]
        # )

