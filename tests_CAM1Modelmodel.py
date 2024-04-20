import unittest
from unittest.mock import patch
from datetime import datetime


from assessment.models import CAM1Model


class TestCAM1ModelWithoutDB(unittest.TestCase):
    @patch("assessment.models.CAM1Model")
    def test_cam1_model_logic(self, MockCAM1Model):

        cam1_instance = MockCAM1Model()
        cam1_instance.patientName = "Test Patient"
        cam1_instance.my_datetime_field = datetime.now()
        cam1_instance.checkbox1 = False
        cam1_instance.checkbox2 = False
        cam1_instance.checkbox3 = False
        cam1_instance.checkbox4 = False
        cam1_instance.checkbox5 = True
        cam1_instance.checkbox6 = False


if __name__ == "__main__":
    unittest.main()
