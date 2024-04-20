from unittest.mock import patch

from django.test import SimpleTestCase

from assessment.forms import PrePostForm
from assessment.identifiers import Sign


class TestPrePostForm(SimpleTestCase):
    def setUp(self):
        self.form_data = {
            'TherapistEmail': 'therapist@example.com',
            'VITALSExistsInEPIC': Sign.Positive,
            'VITALSSingle': 'Example Vitals',
            'BPExistsInEPIC': Sign.Positive,
            'BPSingle': '120/80',
            'BPLocationExistsInEPIC': Sign.Positive,
            'BPLocationSingle': 'Arm',
            'PatientPositionExistsInEPIC': Sign.Positive,
            'PatientPositionSingle': 'Sitting',
            'HRExistsInEPIC': Sign.Positive,
            'HRSingle': '72',
            'RRExistsInEPIC': Sign.Positive,
            'RRSingle': '18',
            'O2ExistsInEPIC': Sign.Positive,
            'O2Single': '98%',
            'PulseExistsInEPIC': Sign.Positive,
            'PulseSingle': '72',
            'PulseOxLocationExistsInEPIC': Sign.Positive,
            'PulseOxLocationSingle': 'Finger',
        }

    @patch('assessment.forms.send_mail')
    def test_send_email_without_database(self, mock_send_mail):
        form = PrePostForm(data=self.form_data)
        self.assertTrue(form.is_valid(), msg=form.errors)


        form.send()


        mock_send_mail.assert_called_once()
        args, kwargs = mock_send_mail.call_args


        self.assertEqual(kwargs['subject'], 'Pre/Post Tests')
        self.assertIn('PrePostForm', kwargs['html_message'])
        self.assertEqual(kwargs['recipient_list'], ['therapist@example.com'])

    def test_get_info_method(self):
        form = PrePostForm(data=self.form_data)
        self.assertTrue(form.is_valid(), msg=form.errors)

        subject, msg, recipient = form.get_info()

        self.assertEqual(subject, 'Pre/Post Tests')
        self.assertIn('PrePostForm', msg)
        self.assertEqual(recipient, 'therapist@example.com')
