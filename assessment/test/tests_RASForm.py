
from django.test import SimpleTestCase, TestCase

from assessment.forms import RASForm


class RASFormTest(SimpleTestCase):
    def setUp(self):
        self.valid_data = {
            'patientName': 'Test Patient',
            'initialWalk': 100.0,
            'firstWalkSteps': 50,
            'firstWalkSeconds': 30,
            'firstCadence': 100.0,
            'firstVelocity': 2.0,
            'firstStrideLength': 1.5,
        }

    def test_form_validity_with_valid_data(self):
        form = RASForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_form_invalidity_with_negative_values(self):
        invalid_data = self.valid_data.copy()
        invalid_data['firstWalkSteps'] = -10  # Invalid negative value
        form = RASForm(data=invalid_data)
        self.assertFalse(form.is_valid())

    """""
    def test_get_info_method(self):
        form = RASForm(data=self.valid_data)
        if form.is_valid():
            title, result = form.get_info()
            self.assertIn('RasForm/Evaluation', title)
            self.assertIn('description', result)  # This checks if 'description' is part of the context used in the template.
"""""
