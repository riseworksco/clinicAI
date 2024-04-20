from unittest import TestCase, mock
from assessment.models import PsychoemotionalScreeningRecord


class TestPsychoemotionalScreeningRecordModelWithoutDB(TestCase):
    @mock.patch("assessment.models.PsychoemotionalScreeningRecord")
    @mock.patch("assessment.models.Doctor")
    @mock.patch("assessment.models.Patient")
    @mock.patch("assessment.models.GAD2")
    @mock.patch("assessment.models.GAD7")
    @mock.patch("assessment.models.PHQ2")
    @mock.patch("assessment.models.PHQ9")
    def test_psychoemotional_screening_record_creation(
        self,
        MockPHQ9,
        MockPHQ2,
        MockGAD7,
        MockGAD2,
        MockPatient,
        MockDoctor,
        MockScreeningRecord,
    ):

        doctor_instance = MockDoctor()
        patient_instance = MockPatient()

        gad2_instance = MockGAD2()
        gad7_instance = MockGAD7()
        phq2_instance = MockPHQ2()
        phq9_instance = MockPHQ9()

        screening_record_instance = MockScreeningRecord()
        screening_record_instance.doctor = doctor_instance
        screening_record_instance.patient = patient_instance
        screening_record_instance.GAD2 = gad2_instance
        screening_record_instance.GAD7 = gad7_instance
        screening_record_instance.PHQ2 = phq2_instance
        screening_record_instance.PHQ9 = phq9_instance

        self.assertIs(
            screening_record_instance.doctor,
            doctor_instance,
            "Doctor instance should be associated correctly",
        )
        self.assertIs(
            screening_record_instance.patient,
            patient_instance,
            "Patient instance should be associated correctly",
        )
        self.assertIs(
            screening_record_instance.GAD2,
            gad2_instance,
            "GAD2 instance should be associated correctly",
        )
        self.assertIs(
            screening_record_instance.GAD7,
            gad7_instance,
            "GAD7 instance should be associated correctly",
        )
        self.assertIs(
            screening_record_instance.PHQ2,
            phq2_instance,
            "PHQ2 instance should be associated correctly",
        )
        self.assertIs(
            screening_record_instance.PHQ9,
            phq9_instance,
            "PHQ9 instance should be associated correctly",
        )
