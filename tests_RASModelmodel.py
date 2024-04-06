from unittest import TestCase, mock
from django.template.loader import render_to_string
from assessment.models import RASModel


class TestRASModelWithoutDB(TestCase):
    def setUp(self):

        self.ras_data = {
            'patientName': 'John Doe',
            'initialWalk': 100.0,
            'firstWalkSteps': 50,
            'firstWalkSeconds': 30,
            'firstCadence': 60.0,
            'firstVelocity': 2.0,
            'firstStrideLength': 1.0
        }

    @mock.patch('assessment.models.RASModel')
    def test_get_info_logic(self, MockRASModel):

        ras_instance = MockRASModel()


        for attr, value in self.ras_data.items():
            setattr(ras_instance, attr, value)


        ras_instance.get_info.return_value = ('RasForm/Evaluation', 'Mocked Result')


        header, result = ras_instance.get_info()

        self.assertEqual(header, 'RasForm/Evaluation')
        self.assertEqual(result, 'Mocked Result')


        ras_instance.get_info.assert_called_once()
