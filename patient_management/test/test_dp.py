"""
from django.test import TestCase
from unittest.mock import create_autospec
from django.contrib.auth.models import User
from patient_management.models import Doctor, Patient  # Adjust 'yourapp' to the actual name of your Django app

class DoctorModelTest(TestCase):

    def setUp(self):
        # Mock the User object for the Doctor model
        self.user = create_autospec(User, username='doctor_username')
        self.doctor = Doctor(user=self.user)

    def test_doctor_str(self):
        # Test the __str__ method of Doctor model
        self.assertEqual(str(self.doctor), 'doctor_username')

class PatientModelTest(TestCase):

    def setUp(self):
        # Mock the User object for both Doctor and Patient models
        doctor_user = create_autospec(User, username='doctor_username')
        patient_user = create_autospec(User, username='patient_username')
        self.doctor = Doctor(user=doctor_user)
        self.patient = Patient(user=patient_user, doctor=self.doctor)

    def test_patient_str(self):
        # Test the __str__ method of Patient model
        self.assertEqual(str(self.patient), 'patient_username')

    def test_patient_doctor_relationship(self):
        # Test the doctor assigned to the patient is correct
        self.assertEqual(self.patient.doctor, self.doctor)
"""
