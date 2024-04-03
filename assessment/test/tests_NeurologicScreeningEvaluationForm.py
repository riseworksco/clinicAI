from django.test import SimpleTestCase
from assessment.forms import NeurologicScreeningEvaluationForm
from unittest.mock import patch
from assessment.identifiers import Sign


class TestNeurologicScreeningEvaluationForm(SimpleTestCase):
    def setUp(self):
        self.form_data = {
            'TherapistEmail': 'therapist@example.com',
            'feature1': Sign.Positive,
            'feature1ExistsInEPIC': Sign.Positive,
            'feature1Single': 'Test Feature 1',
            'feature2': Sign.Negative,
            'feature2ExistsInEPIC': Sign.Negative,
            'feature2Single': 'Test Feature 2',
            'feature3': Sign.Positive,
            'feature3ExistsInEPIC': Sign.Positive,
            'feature3Single': 'Test Feature 3',
            'feature4': Sign.Negative,
            'feature4ExistsInEPIC': Sign.Negative,
            'feature4Single': 'Test Feature 4',
        }

    @patch('assessment.forms.send_mail')
    def test_send_email_without_database(self, mock_send_mail):
        form = NeurologicScreeningEvaluationForm(data=self.form_data)
        self.assertTrue(form.is_valid(), msg=form.errors)


        form.send()


        mock_send_mail.assert_called_once()
        args, kwargs = mock_send_mail.call_args


        self.assertEqual(kwargs['subject'], 'Neurologic Screening/Evaluation')
        self.assertIn('Neurologic Screening/Evaluation', kwargs['html_message'])
        self.assertEqual(kwargs['recipient_list'], ['therapist@example.com'])

    def test_get_info_method(self):
        form = NeurologicScreeningEvaluationForm(data=self.form_data)
        self.assertTrue(form.is_valid(), msg=form.errors)

        subject, msg, recipient = form.get_info()

        self.assertEqual(subject, 'Neurologic Screening/Evaluation')
        self.assertIn('Neurologic Screening/Evaluation', msg)
        self.assertEqual(recipient, 'therapist@example.com')
