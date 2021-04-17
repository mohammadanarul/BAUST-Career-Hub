from django.db import models

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name =models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    std_id = models.IntegerField()
    level = models.IntegerField()
    term = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    photo = models.FileField()

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50)
    name =models.CharField(max_length=50)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    photo = models.FileField()