from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser



class Person(models.Model):
    f_name = models.CharField(max_length=30)
    m_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    Mobile = PhoneNumberField(region='IN')
    e_mail = models.EmailField(max_length=254,  blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    birthdate = models.DateField(blank=True)

    def __str__(self):
        return 'Person name : {}'.format(self.f_name)

class Patient(Person):
    pat_reg_date = models.DateField()

    def __str__(self):
        return 'Patient name : {}'.format(self.f_name)


class User(Person):
    user_name = models.CharField(max_length=30)
    user_pw = models.CharField(max_length=30)
    u_reg_date = models.DateField()

    def __str__(self):
        return 'User with Username : {}'.format(self.user_name)

class Medical_History(models.Model):
    complains = models.CharField(max_length=500)
    



class Consultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='opd_patient')
    consult_datetime = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return 'OPD consultation of {} on {} '.format(self.patient, self.consult_date)

    



