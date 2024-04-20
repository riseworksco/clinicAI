from unittest import TestCase, mock
from assessment.models import CatCatFlowsheetRecord


class TestCatCatFlowsheetRecordWithoutDB(TestCase):
    def test_calculate_total_smf(self):

        with mock.patch(
            "assessment.models.CatCatFlowsheetRecord"
        ) as MockCatCatFlowsheetRecord:

            record_mock = MockCatCatFlowsheetRecord()
            record_mock.type1_smf = 1
            record_mock.type2_smf = 2
            record_mock.type3_smf = 3
            record_mock.type4_smf = 4

            record_mock.calculate_total_smf.return_value = 10

            total_smf = record_mock.calculate_total_smf()

            self.assertEqual(total_smf, 10)

            record_mock.calculate_total_smf.assert_called_once()
