
from django.test import SimpleTestCase, override_settings
from django.core import mail
from assessment.forms import AT4Form
from unittest.mock import patch
from django.conf import settings


class TestAT4Form(SimpleTestCase):
    def setUp(self):
        self.valid_data = {
            'TherapistEmail': 'therapist@example.com',
            'patientName': 'John Doe',
            'patientNumber': '12345',
            'birthDate': '2000-01-01',
            'my_datetime_field': '2000-01-01T12:00',
            'TesterName': 'Tester',
            'question1': '0',
            'question2': '0',
            'question3': '0',
            'question4': '0',
            'AtScore': 0.0,
        }

    def test_form_is_valid(self):
        form = AT4Form(data=self.valid_data)
        self.assertTrue(form.is_valid())

    """""
    @patch('assessment.forms.send_mail')
    def test_send_email(self, mock_send_mail):
        form = AT4Form(data=self.valid_data)
        self.assertTrue(form.is_valid())

        form.send()

        mock_send_mail.assert_called_once()
        args, kwargs = mock_send_mail.call_args
        self.assertEqual(kwargs['subject'], 'RasForm/Evaluation')
        self.assertIn('therapist@example.com', kwargs['recipient_list'])
        self.assertIn('html_message', kwargs)
        self.assertTrue(len(mail.outbox) == 1)
        self.assertEqual(mail.outbox[0].subject, 'RasForm/Evaluation')

    def test_get_info(self):
        form = AT4Form(data=self.valid_data)
        self.assertTrue(form.is_valid())

        subject, result, recipient = form.get_info()

        self.assertEqual(subject, 'RasForm/Evaluation')
        self.assertEqual(recipient, 'therapist@example.com')
        self.assertIn('RasForm/Evaluation', result)


"""""
