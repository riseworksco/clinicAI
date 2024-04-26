import datetime
from datetime import date
from unittest.mock import patch

from django.core import mail
from django.test import SimpleTestCase, override_settings

from assessment.forms import AAQ2Form


class TestAAQ2Form(SimpleTestCase):
    def setUp(self):
        self.valid_data = {
            "name": "John Doe",
            "date": date.today(),
            "question1": "1",
            "question2": "2",
            "question3": "3",
            "question4": "4",
            "question5": "5",
            "question6": "6",
            "question7": "7",
        }

    def test_form_is_valid(self):
        form = AAQ2Form(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_calculate_total_score(self):
        form = AAQ2Form(data=self.valid_data)
        if form.is_valid():
            total_score = form.calculate_total_score()
            self.assertEqual(total_score, 28)  # Adjust based on expected total score

    def test_get_diagnosis(self):
        form = AAQ2Form(data=self.valid_data)
        if form.is_valid():
            total_score = form.calculate_total_score()
            diagnosis = form.get_diagnosis(total_score)
            self.assertIn("Probable current clinical distress", diagnosis)


"""""
    @patch('assessment.forms.send_mail')
    def test_send_email(self, mock_send_mail):
        form = AAQ2Form(data=self.valid_data)
        self.assertTrue(form.is_valid())

        form.send()

        mock_send_mail.assert_called_once()
        args, kwargs = mock_send_mail.call_args
        self.assertEqual(kwargs['subject'], 'AAQIIForm/Evaluation')
        self.assertIn('John Doe', kwargs['html_message'])
        self.assertIn(kwargs['recipient_list'], ['therapist@example.com'])

    def test_get_info_method(self):
        form = AAQ2Form(data=self.valid_data)
        self.assertTrue(form.is_valid())

        subject, msg, recipient = form.get_info()

        self.assertEqual(subject, 'AAQIIForm/Evaluation')
        self.assertIn('AAQIIForm/Evaluation', msg)
        self.assertEqual(recipient, 'therapist@example.com')  # Make sure this matches the actual recipient field


""" ""
