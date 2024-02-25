from django.db import models

from patient_management.models import Doctor, Patient


# Create your models here.
class Stomp(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    Alternative = models.IntegerField()
    Bluegrass = models.IntegerField()
    Blues = models.IntegerField()
    Classical = models.IntegerField()
    Country = models.IntegerField()
    Dance_Electronica = models.IntegerField()
    Folk = models.IntegerField()
    Funk = models.IntegerField()
    Gospel = models.IntegerField()
    Heavy_Meta = models.IntegerField()
    World = models.IntegerField()


# PsychoemotionalScreeningRecord stuffs
class GAD2(models.Model):
    # 1. Feeling nervous, anxious on edge
    q1_value = models.IntegerField()
    q1_epic = models.CharField('No', max_length=30)
    q1_smf = models.IntegerField()

    q2_value = models.IntegerField()
    q2_epic = models.IntegerField()
    q2_smf = models.IntegerField()

    # Score
    score = models.IntegerField()  # Total Number
    score_epic = models.CharField('No', max_length=30)
    score_smf = models.CharField('FR', max_length=30)

    # Interpretation
    interpretation = models.TextField()
    interpretation_epic = models.CharField('No', max_length=30)
    interpretation_smf = models.CharField('FR', max_length=30)


class GAD7(models.Model):
    q1_value = models.IntegerField()
    q1_epic = models.CharField('No', max_length=30)
    q1_smf = models.IntegerField()

    q2_value = models.IntegerField()
    q2_epic = models.IntegerField()
    q2_smf = models.IntegerField()

    q3_value = models.IntegerField()
    q3_epic = models.CharField('No', max_length=30)
    q3_smf = models.IntegerField()

    q4_value = models.IntegerField()
    q4_epic = models.IntegerField()
    q4_smf = models.IntegerField()

    q5_value = models.IntegerField()
    q5_epic = models.CharField('No', max_length=30)
    q5_smf = models.IntegerField()

    q6_value = models.IntegerField()
    q6_epic = models.IntegerField()
    q6_smf = models.IntegerField()

    q7_value = models.IntegerField()
    q7_epic = models.IntegerField()
    q7_smf = models.IntegerField()

    # Score
    score = models.IntegerField()  # Total Number
    score_epic = models.CharField('No', max_length=30)
    score_smf = models.CharField('FR', max_length=30)

    # Interpretation
    interpretation = models.TextField()
    interpretation_epic = models.CharField('No', max_length=30)
    interpretation_smf = models.CharField('FR', max_length=30)


class PHQ2(models.Model):
    # 1. Feeling nervous, anxious on edge
    q1_value = models.IntegerField()
    q1_epic = models.CharField('No', max_length=30)
    q1_smf = models.CharField('No', max_length=30)

    q2_value = models.IntegerField()
    q2_epic = models.IntegerField()
    q2_smf = models.IntegerField()

    # Score
    score = models.IntegerField()  # Total Number
    score_epic = models.CharField('No', max_length=30)
    score_smf = models.CharField('FR', max_length=30)

    # Interpretation
    interpretation = models.TextField()
    interpretation_epic = models.CharField('No', max_length=30)
    interpretation_smf = models.CharField('FR', max_length=30)


class PHQ9(models.Model):
    q1_value = models.IntegerField()
    q1_epic = models.CharField('No', max_length=30)
    q1_smf = models.IntegerField()

    q2_value = models.IntegerField()
    q2_epic = models.IntegerField()
    q2_smf = models.IntegerField()

    q3_value = models.IntegerField()
    q3_epic = models.CharField('No', max_length=30)
    q3_smf = models.IntegerField()

    q4_value = models.IntegerField()
    q4_epic = models.IntegerField()
    q4_smf = models.IntegerField()

    q5_value = models.IntegerField()
    q5_epic = models.CharField('No''No', max_length=30)
    q5_smf = models.IntegerField()

    q6_value = models.IntegerField()
    q6_epic = models.IntegerField()
    q6_smf = models.IntegerField()

    q7_value = models.IntegerField()
    q7_epic = models.IntegerField()
    q7_smf = models.IntegerField()

    # Score
    score = models.IntegerField()  # Total Number
    score_epic = models.CharField('No', max_length=30)
    score_smf = models.CharField('FR', max_length=30)

    # Interpretation
    interpretation = models.TextField()
    interpretation_epic = models.CharField('No', max_length=30)
    interpretation_smf = models.CharField('FR', max_length=30)


class PsychoemotionalScreeningRecord(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    GAD2 = models.OneToOneField(GAD2, on_delete=models.CASCADE, )
    GAD7 = models.OneToOneField(GAD7, on_delete=models.CASCADE, )
    PHQ2 = models.OneToOneField(PHQ2, on_delete=models.CASCADE, )
    PHQ9 = models.OneToOneField(PHQ9, on_delete=models.CASCADE, )


class CatCatFlowsheetRecord(models.Model):
    """
    CatCatFlowsheetRecord
    """
    type1_value = models.CharField('eval', max_length=30)
    type1_epic = models.CharField('No', max_length=30)
    type1_smf = models.IntegerField()

    type2_value = models.CharField('treatment', max_length=30)
    type2_epic = models.CharField('No', max_length=30)
    type2_smf = models.IntegerField()

    type3_value = models.CharField('treatment pre', max_length=30)
    type3_epic = models.CharField('No', max_length=30)
    type3_smf = models.IntegerField()

    type4_value = models.CharField('treatment post', max_length=30)
    type4_epic = models.CharField('No', max_length=30)
    type4_smf = models.IntegerField()