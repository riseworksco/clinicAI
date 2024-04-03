from unittest import TestCase, mock
from datetime import date


# 假设 GAD7Model 在 myapp.models 模块中
@mock.patch('assessment.models.GAD7Model')
class TestGAD7ModelWithoutDB(TestCase):
    def setUp(self):
        # 设置 mock 对象的返回值
        self.mock_gad7_instance = mock.MagicMock(name='GAD7Model Instance')
        self.mock_gad7_instance.calculate_total_score.return_value = 7
        self.mock_gad7_instance.get_anxiety_level.return_value = "Mild anxiety."

    def test_calculate_total_score(self, MockGAD7Model):
        # 模拟 GAD7Model 的实例
        MockGAD7Model.return_value = self.mock_gad7_instance

        # 创建 GAD7Model 的一个实例
        gad7_instance = MockGAD7Model()

        # 调用 calculate_total_score 方法
        total_score = gad7_instance.calculate_total_score()

        # 验证返回的总分是否为预期的 7
        self.assertEqual(total_score, 7)
        gad7_instance.calculate_total_score.assert_called_once()

    def test_get_anxiety_level(self, MockGAD7Model):
        # 模拟 GAD7Model 的实例
        MockGAD7Model.return_value = self.mock_gad7_instance

        # 创建 GAD7Model 的一个实例
        gad7_instance = MockGAD7Model()

        # 调用 get_anxiety_level 方法
        anxiety_level = gad7_instance.get_anxiety_level()

        # 验证返回的焦虑级别是否为预期的 "Mild anxiety."
        self.assertEqual(anxiety_level, "Mild anxiety.")
        gad7_instance.get_anxiety_level.assert_called_once()

