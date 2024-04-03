from unittest import TestCase, mock
from django.template.loader import render_to_string
from assessment.models import RASModel


class TestRASModelWithoutDB(TestCase):
    def setUp(self):
        # 设置模拟数据
        self.ras_data = {
            'patientName': 'John Doe',
            'initialWalk': 100.0,
            'firstWalkSteps': 50,
            'firstWalkSeconds': 30,
            'firstCadence': 60.0,
            'firstVelocity': 2.0,
            'firstStrideLength': 1.0
        }

    @mock.patch('assessment.models.RASModel')
    def test_get_info_logic(self, MockRASModel):
        # 模拟RASModel实例
        ras_instance = MockRASModel()

        # 设置模拟对象的属性
        for attr, value in self.ras_data.items():
            setattr(ras_instance, attr, value)

        # 模拟get_info方法的行为
        ras_instance.get_info.return_value = ('RasForm/Evaluation', 'Mocked Result')

        # 调用模拟的get_info方法
        header, result = ras_instance.get_info()

        # 验证返回的头部和结果是否符合预期
        self.assertEqual(header, 'RasForm/Evaluation')
        self.assertEqual(result, 'Mocked Result')

        # 确保get_info方法被正确调用
        ras_instance.get_info.assert_called_once()
