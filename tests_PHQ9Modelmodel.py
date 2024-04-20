import unittest
from unittest.mock import Mock
from django.core.exceptions import ValidationError
import datetime


class TestPHQ9ModelWithoutDB(unittest.TestCase):

    def setUp(self):

        self.phq9_mock = Mock()
        self.phq9_mock.name = "Test User"
        self.phq9_mock.date = datetime.date.today()
        self.phq9_mock.question1 = "1"
        self.phq9_mock.question2 = "2"
        self.phq9_mock.question3 = "3"
        self.phq9_mock.question4 = "2"
        self.phq9_mock.question5 = "1"
        self.phq9_mock.question6 = "2"
        self.phq9_mock.question7 = "3"
        self.phq9_mock.question8 = "1"
        self.phq9_mock.question9 = "2"

        self.phq9_mock.calculate_total_score.return_value = 17

        self.phq9_mock.get_diagnosis.return_value = "Moderate depression"

    def test_calculate_total_score(self):
        total_score = self.phq9_mock.calculate_total_score()
        self.phq9_mock.calculate_total_score.assert_called_once()
        self.assertEqual(total_score, 17)

    def test_get_diagnosis(self):
        diagnosis = self.phq9_mock.get_diagnosis(total_score=17)
        self.phq9_mock.get_diagnosis.assert_called_once_with(total_score=17)
        self.assertEqual(diagnosis, "Moderate depression")

    def test_clean_method_raises_validation_error(self):

        self.phq9_mock.clean.side_effect = ValidationError(
            {"name": "Name cannot be empty."}
        )
        with self.assertRaises(ValidationError):
            self.phq9_mock.clean()


if __name__ == "__main__":
    unittest.main()
