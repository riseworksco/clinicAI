from unittest import TestCase, mock
from datetime import date


@mock.patch("assessment.models.GAD7Model")
class TestGAD7ModelWithoutDB(TestCase):
    def setUp(self):

        self.mock_gad7_instance = mock.MagicMock(name="GAD7Model Instance")
        self.mock_gad7_instance.calculate_total_score.return_value = 7
        self.mock_gad7_instance.get_anxiety_level.return_value = "Mild anxiety."

    def test_calculate_total_score(self, MockGAD7Model):

        MockGAD7Model.return_value = self.mock_gad7_instance

        gad7_instance = MockGAD7Model()

        total_score = gad7_instance.calculate_total_score()

        self.assertEqual(total_score, 7)
        gad7_instance.calculate_total_score.assert_called_once()

    def test_get_anxiety_level(self, MockGAD7Model):

        MockGAD7Model.return_value = self.mock_gad7_instance

        gad7_instance = MockGAD7Model()

        anxiety_level = gad7_instance.get_anxiety_level()

        # 验证返回的焦虑级别是否为预期的 "Mild anxiety."
        self.assertEqual(anxiety_level, "Mild anxiety.")
        gad7_instance.get_anxiety_level.assert_called_once()
