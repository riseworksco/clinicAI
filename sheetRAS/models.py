import logging

from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

class RasModel(models.Model):
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

        logging.info(form.data)
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

