"""""
from django.test import TestCase
from assessment.forms import PsychoemotionalScreeningEvaluationForm
from assessment.models import PsychoemotionalScreeningRecord
from django.contrib.auth.models import User


class PsychoemotionalScreeningEvaluationFormTest(TestCase):

    def setUp(self):

        self.doctor = User.objects.create_user(username='doctor_test', password='12345')
        self.patient = User.objects.create_user(username='patient_test', password='12345')


        self.record = PsychoemotionalScreeningRecord.objects.create(doctor=self.doctor, patient=self.patient)

    def test_form_validity(self):

        form_data = {
            'doctor': self.doctor.id,
            'patient': self.patient.id
        }
        form = PsychoemotionalScreeningEvaluationForm(data=form_data)


        self.assertTrue(form.is_valid())

    def test_form_save(self):

        form_data = {
            'doctor': self.doctor.id,
            'patient': self.patient.id
        }
        form = PsychoemotionalScreeningEvaluationForm(data=form_data)


        if form.is_valid():
            new_record = form.save()
            self.assertIsInstance(new_record, PsychoemotionalScreeningRecord)
            self.assertEqual(new_record.doctor, self.doctor)
            self.assertEqual(new_record.patient, self.patient)
"""""
