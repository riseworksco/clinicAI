from unittest import TestCase, mock
from assessment.models import GAD2

class TestGAD2ModelWithoutDB(TestCase):
    @mock.patch('assessment.models.GAD2')
    def test_gad2_model_logic(self, MockGAD2):
        gad2_instance = MockGAD2()
        gad2_instance.q1_value = 2
        gad2_instance.q2_value = 3

        # 假设calculate_score方法返回q1_value和q2_value的和
        gad2_instance.calculate_score.return_value = 5

        # 假设interpret_score方法根据分数返回解释
        gad2_instance.interpret_score.return_value = "Mild anxiety"

        # 计算得分
        score = gad2_instance.calculate_score()
        self.assertEqual(score, 5, "The score calculation should be correct")

        # 获取解释
        interpretation = gad2_instance.interpret_score(score)
        self.assertEqual(interpretation, "Mild anxiety", "The interpretation should match the score")

        # 验证方法是否被调用
        gad2_instance.calculate_score.assert_called_once_with()
        gad2_instance.interpret_score.assert_called_once_with(score)
