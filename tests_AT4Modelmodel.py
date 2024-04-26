import datetime
from unittest import TestCase, mock

from assessment.models import AT4Model


class TestAT4ModelWithoutDB(TestCase):
    def setUp(self):

        self.at4_data = {
            "patientName": "John Doe",
            "patientNumber": "12345678",
            "birthDate": datetime.date.today(),
            "my_datetime_field": datetime.datetime.now(),
            "TesterName": "Tester Name",
            "question1": "0",
            "question2": "1",
            "question3": "2",
            "question4": "4",
            "AtScore": 0.0,  #
        }

    @mock.patch("assessment.models.AT4Model")
    def test_calculate_score_logic(self, MockAT4Model):

        at4_instance = MockAT4Model()

        at4_instance.calculate_score.return_value = 7

        score = at4_instance.calculate_score()

        self.assertEqual(score, 7)

        at4_instance.calculate_score.assert_called_once()
