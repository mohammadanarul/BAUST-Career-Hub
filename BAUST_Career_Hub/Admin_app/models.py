from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    user_type_data = ((1, "Student"), (2, "Teacher"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)





class Student(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(User, on_delete=models.CASCADE)

    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    student_id = models.CharField(max_length=50)
    level_term = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    picture = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(User, on_delete=models.CASCADE)

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


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            Student.objects.create(admin=instance)
        if instance.user_type == 2:
            Teacher.objects.create(admin=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.student.save()
    if instance.user_type == 2:
        instance.teacher.save()