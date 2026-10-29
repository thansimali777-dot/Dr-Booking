from django.db import models

# Create your models here.


class Doctor_table(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    specialization=models.CharField(max_length=500)

class Schedule_table(models.Model):
    DOCTOR=models.ForeignKey(Doctor_table,on_delete=models.CASCADE)
    days = models.DateField()
    fromtime = models.TimeField()
    totime = models.TimeField()
    status=models.CharField(max_length=100)

class User_table(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

class Booking_table(models.Model):
    SCHEDULE=models.ForeignKey(Schedule_table,on_delete=models.CASCADE)
    USER=models.ForeignKey(User_table,on_delete=models.CASCADE)
    date=models.DateField()
    status=models.CharField(max_length=100)






