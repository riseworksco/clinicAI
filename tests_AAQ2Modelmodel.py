import unittest
from unittest.mock import Mock
import datetime


class TestAAQ2ModelWithoutDB(unittest.TestCase):
    def setUp(self):

        self.aaq2_mock = Mock()
        self.aaq2_mock.name = 'Test User'
        self.aaq2_mock.date = datetime.date.today()
        self.aaq2_mock.question1 = '1'
        self.aaq2_mock.question2 = '2'
        self.aaq2_mock.question3 = '3'
        self.aaq2_mock.question4 = '4'
        self.aaq2_mock.question5 = '5'
        self.aaq2_mock.question6 = '6'
        self.aaq2_mock.question7 = '7'


        self.aaq2_mock.calculate_total_score.return_value = 28


        self.aaq2_mock.get_diagnosis.return_value = "Probable current clinical distress, future distress & work absence more likely."

    def test_calculate_total_score(self):
        total_score = self.aaq2_mock.calculate_total_score()
        self.aaq2_mock.calculate_total_score.assert_called_once()
        self.assertEqual(total_score, 28)

    def test_get_diagnosis(self):
        diagnosis = self.aaq2_mock.get_diagnosis()
        self.aaq2_mock.get_diagnosis.assert_called_once()
        self.assertEqual(diagnosis, "Probable current clinical distress, future distress & work absence more likely.")


if __name__ == '__main__':
    unittest.main()
