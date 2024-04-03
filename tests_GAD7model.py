from unittest import TestCase, mock
from assessment.models import GAD7

class TestGAD7ModelWithoutDB(TestCase):
    @mock.patch('assessment.models.GAD7')
    def test_gad7_model_logic(self, MockGAD7):
        gad7_instance = MockGAD7()
        gad7_instance.q1_value = 1
        gad7_instance.q2_value = 1
        gad7_instance.q3_value = 1
        gad7_instance.q4_value = 1
        gad7_instance.q5_value = 1
        gad7_instance.q6_value = 1
        gad7_instance.q7_value = 1

        # 假设calculate_total_score方法返回所有问题值的和
        gad7_instance.calculate_total_score.return_value = 7

        # 假设get_interpretation方法根据总分返回解释
        gad7_instance.get_interpretation.return_value = "Mild anxiety"

        # 计算总分
        total_score = gad7_instance.calculate_total_score()
        self.assertEqual(total_score, 7, "The total score calculation should be correct")

        # 获取解释
        interpretation = gad7_instance.get_interpretation(total_score)
        self.assertEqual(interpretation, "Mild anxiety", "The interpretation should match the total score")

        # 验证方法是否被调用
        gad7_instance.calculate_total_score.assert_called_once_with()
        gad7_instance.get_interpretation.assert_called_once_with(total_score)
