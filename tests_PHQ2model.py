from unittest import TestCase, mock
from assessment.models import PHQ2


class TestPHQ2ModelWithoutDB(TestCase):
    @mock.patch("assessment.models.PHQ2")
    def test_phq2_model_logic(self, MockPHQ2):
        phq2_instance = MockPHQ2()
        phq2_instance.q1_value = 2
        phq2_instance.q2_value = 1

        phq2_instance.calculate_total_score.return_value = 3

        expected_interpretation = "Minimal depression"
        phq2_instance.get_interpretation.return_value = expected_interpretation

        total_score = phq2_instance.calculate_total_score()
        self.assertEqual(
            total_score, 3, "The total score calculation should be correct"
        )

        interpretation = phq2_instance.get_interpretation(total_score)
        self.assertEqual(
            interpretation,
            expected_interpretation,
            "The interpretation should match the total score",
        )

        phq2_instance.calculate_total_score.assert_called_once_with()
        phq2_instance.get_interpretation.assert_called_once_with(total_score)
