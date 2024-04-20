from unittest import TestCase, mock
from assessment.models import GAD7


class TestGAD7ModelWithoutDB(TestCase):
    @mock.patch("assessment.models.GAD7")
    def test_gad7_model_logic(self, MockGAD7):
        gad7_instance = MockGAD7()
        gad7_instance.q1_value = 1
        gad7_instance.q2_value = 1
        gad7_instance.q3_value = 1
        gad7_instance.q4_value = 1
        gad7_instance.q5_value = 1
        gad7_instance.q6_value = 1
        gad7_instance.q7_value = 1

        gad7_instance.calculate_total_score.return_value = 7

        gad7_instance.get_interpretation.return_value = "Mild anxiety"

        total_score = gad7_instance.calculate_total_score()
        self.assertEqual(
            total_score, 7, "The total score calculation should be correct"
        )

        interpretation = gad7_instance.get_interpretation(total_score)
        self.assertEqual(
            interpretation,
            "Mild anxiety",
            "The interpretation should match the total score",
        )

        gad7_instance.calculate_total_score.assert_called_once_with()
        gad7_instance.get_interpretation.assert_called_once_with(total_score)
