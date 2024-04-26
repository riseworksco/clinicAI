from unittest import TestCase, mock

from assessment.models import PHQ9


class TestPHQ9ModelWithoutDB(TestCase):
    @mock.patch("assessment.models.PHQ9")
    def test_phq9_model_logic(self, MockPHQ9):
        phq9_instance = MockPHQ9()

        phq9_instance.q1_value = 2
        phq9_instance.q2_value = 1

        phq9_instance.calculate_total_score.return_value = 10

        expected_interpretation = "Mild depression"
        phq9_instance.get_interpretation.return_value = expected_interpretation

        total_score = phq9_instance.calculate_total_score()
        self.assertEqual(
            total_score, 10, "The total score calculation should be correct"
        )

        interpretation = phq9_instance.get_interpretation(total_score)
        self.assertEqual(
            interpretation,
            expected_interpretation,
            "The interpretation should match the total score",
        )

        phq9_instance.calculate_total_score.assert_called_once_with()
        phq9_instance.get_interpretation.assert_called_once_with(total_score)
