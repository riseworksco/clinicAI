from unittest import TestCase, mock
from assessment.models import Stomp

class TestStompModelWithoutDB(TestCase):
    @mock.patch('assessment.models.Stomp')
    def test_stomp_model_logic(self, MockStomp):

        stomp_instance = MockStomp()
        stomp_instance.Alternative = 5
        stomp_instance.Bluegrass = 4

        stomp_instance.calculate_total.return_value = 9


        total = stomp_instance.calculate_total()


        self.assertEqual(total, 9)

        stomp_instance.calculate_total.assert_called_once_with()

