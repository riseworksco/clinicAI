
from datetime import date
from unittest.mock import patch

from django.forms import ValidationError
from django.test import SimpleTestCase

from assessment.forms import GAD7Form


class TestGAD7Form(SimpleTestCase):
    def setUp(self):
        self.form_data = {
            'name': 'Test User',
            'date': date.today(),
            'question1': '1',
            'question2': '2',
            'question3': '1',
            'question4': '3',
            'question5': '1',
            'question6': '2',
            'question7': '3',
            'question8': '1',
        }

    def test_form_is_valid(self):
        form = GAD7Form(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_calculate_total_score(self):
        form = GAD7Form(data=self.form_data)
        if form.is_valid():
            total_score = form.calculate_total_score()
            expected_score = sum(int(self.form_data[f'question{i}']) for i in range(1, 8))
            self.assertEqual(total_score, expected_score)

    def test_get_anxiety_level(self):
        form = GAD7Form(data=self.form_data)
        if form.is_valid():
            total_score = form.calculate_total_score()
            anxiety_level = form.get_anxiety_level(total_score)
            # Based on the setUp values, it's moderate anxiety.
            self.assertEqual(anxiety_level, "Moderate anxiety.")
"""""
    @patch('assessment.forms.send_mail')
    def test_send_method(self, mock_send_mail):
        form = GAD7Form(data=self.form_data)
        if form.is_valid():
            form.send()
            mock_send_mail.assert_called_once()
            args, kwargs = mock_send_mail.call_args
            self.assertIn('GAD7Form/Evaluation', kwargs['subject'])
            self.assertIn('recipient_list', kwargs)
"""""
