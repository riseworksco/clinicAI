from datetime import date
from unittest.mock import patch

from django.test import SimpleTestCase

from assessment.forms import PHQ9Form


class TestPHQ9Form(SimpleTestCase):
    def setUp(self):
        self.form_data = {
            "name": "John Doe",
            "date": date.today(),
            "question1": "1",
            "question2": "2",
            "question3": "3",
            "question4": "1",
            "question5": "2",
            "question6": "3",
            "question7": "1",
            "question8": "2",
            "question9": "3",
            "question10": "1",
        }

    def test_form_is_valid(self):
        form = PHQ9Form(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_calculate_total_score(self):
        form = PHQ9Form(data=self.form_data)
        if form.is_valid():
            total_score = form.calculate_total_score()
            # Adjust the expected score based on the form data
            expected_score = 18  # This should match the sum of your question choices
            self.assertEqual(total_score, expected_score)

    def test_get_diagnosis(self):
        form = PHQ9Form(data=self.form_data)
        if form.is_valid():
            total_score = form.calculate_total_score()
            diagnosis = form.get_diagnosis(total_score)
            expected_diagnosis = "Moderately severe depression"
            self.assertEqual(diagnosis, expected_diagnosis)

    """""
    @patch('assessment.forms.send_mail')
    def test_send_method(self, mock_send_mail):
        form = PHQ9Form(data=self.form_data)
        if form.is_valid():
            form.send()
            mock_send_mail.assert_called_once()
            args, kwargs = mock_send_mail.call_args
            self.assertIn('PHQForm/Evaluation', kwargs['subject'])
            self.assertIn('recipient_list', kwargs)
            self.assertTrue(len(kwargs['recipient_list']) == 1)
""" ""
