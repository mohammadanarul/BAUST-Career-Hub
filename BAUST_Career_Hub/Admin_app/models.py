

from django.db import models
from django.db.models.base import Model



class Student(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    student_id = models.CharField(max_length=50)
    level_term = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    #gender = models.CharField(max_length=10)
    #picture = models.FileField()
    #objects = models.Manager()
    #upload_to='../Image/'


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50)
    name =models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    picture = models.FileField()


