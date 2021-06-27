from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    Disease = models.CharField(max_length=70)
    doctor = models.CharField(max_length=50)
    doctor_fees = models.IntegerField(default=500)
    admit_date = models.DateField()