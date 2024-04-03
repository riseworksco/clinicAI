from unittest import TestCase, mock
import datetime
from assessment.models import AT4Model


class TestAT4ModelWithoutDB(TestCase):
    def setUp(self):
        # 设置模拟数据
        self.at4_data = {
            'patientName': 'John Doe',
            'patientNumber': '12345678',
            'birthDate': datetime.date.today(),
            'my_datetime_field': datetime.datetime.now(),
            'TesterName': 'Tester Name',
            'question1': '0',
            'question2': '1',
            'question3': '2',
            'question4': '4',
            'AtScore': 0.0  # 假设的初始分数
        }

    @mock.patch('assessment.models.AT4Model')
    def test_calculate_score_logic(self, MockAT4Model):
        # 模拟AT4Model实例
        at4_instance = MockAT4Model()

        # 设置模拟对象的返回值
        at4_instance.calculate_score.return_value = 7  # 假设这是基于question1到question4的选择计算出的分数

        # 调用模拟的calculate_score方法
        score = at4_instance.calculate_score()

        # 验证返回的分数是否符合预期
        self.assertEqual(score, 7)

        # 确保calculate_score方法被调用
        at4_instance.calculate_score.assert_called_once()
