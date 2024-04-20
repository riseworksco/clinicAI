import datetime
from unittest.mock import patch

from django.test import SimpleTestCase

from assessment.forms import CAM1Form


class TestCAM1Form(SimpleTestCase):
    def setUp(self):
        self.valid_data = {
            'patientName': 'John Doe',
            'my_datetime_field': datetime.datetime.now().strftime('%Y-%m-%dT%H:%M'),
            'checkbox1': True,
            'checkbox2': False,
            'checkbox3': True,
            'checkbox4': False,
            'checkbox5': True,  # Assuming this is the positive condition
            'checkbox6': False,  # And this is the negative condition
        }

    def test_form_is_valid(self):
        form = CAM1Form(data=self.valid_data)
        self.assertTrue(form.is_valid())
"""""
    @patch('assessment.forms.send_mail')
    def test_send_method(self, mock_send_mail):
        form = CAM1Form(data=self.valid_data)
        if form.is_valid():
            form.send()
            # Since send method is commented out, send_mail should not be called
            mock_send_mail.assert_not_called()

    def test_get_info_method(self):
        form = CAM1Form(data=self.valid_data)
        if form.is_valid():
            subject, content = form.get_info()
            self.assertEqual(subject, 'RasForm/Evaluation')
            # Here you can add more assertions related to content or perform more detailed checks.

# Note: Make sure the send_mail is properly mocked or you handle its test if you decide to uncomment it in send method
"""
