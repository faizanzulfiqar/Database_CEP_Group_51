# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bill(models.Model):
    bill_id = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    patient_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    doctor_charges = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    room_charges = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    medicine_charges = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill'


class Diagnosis(models.Model):
    diagnosis_id = models.CharField(primary_key=True, max_length=10)
    patient_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diagnosis'


class Doctor(models.Model):
    doctor_id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    field = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'


class Given(models.Model):
    medicine_id = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    patient_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'given'


class Medicine(models.Model):
    date_end = models.DateTimeField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    medicine_id = models.DecimalField(primary_key=True, max_digits=20, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'medicine'


class Nurse(models.Model):
    nurse_id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'nurse'


class Patient(models.Model):
    patient_id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    f_name = models.CharField(db_column='F_name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    l_name = models.CharField(db_column='L_name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=1, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient'


class Records(models.Model):
    date_admission = models.DateTimeField(blank=True, null=True)
    date_discharge = models.DateTimeField(blank=True, null=True)
    record_id = models.CharField(primary_key=True, max_length=20)
    treatment = models.CharField(max_length=30, blank=True, null=True)
    future_date = models.DateTimeField(blank=True, null=True)
    patient_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    doctor_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'records'


class Room(models.Model):
    room_id = models.CharField(primary_key=True, max_length=10)
    r_type = models.CharField(max_length=20, blank=True, null=True)
    patient_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    nurse_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room'


class Staff(models.Model):
    staff_id = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    fname = models.CharField(max_length=20, blank=True, null=True)
    lname = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)
    phone_no = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'


class Treatment(models.Model):
    patient_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    doctor_id = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treatment'
