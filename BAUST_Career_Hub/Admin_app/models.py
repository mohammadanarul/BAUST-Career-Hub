from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, User
from PIL import Image

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null = True, blank=True)
    phone = models.CharField(max_length=50)
    
    
    
    

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE,  related_name="student")
    student_id = models.CharField(max_length=50)
    level_term = models.ForeignKey('Level_Term', on_delete=models.CASCADE, null = True, blank=True)
    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, related_name="teacher")  
    teacher_id = models.CharField(max_length=50)
    designation = models.ForeignKey('Designation', on_delete=models.CASCADE, null = True, blank=True)
    def __str__(self):
        return self.user.username

class Department(models.Model):
    department_name = models.CharField(max_length=50)
    def __str__(self):
        return self.department_name

class Level_Term(models.Model):
    level_term_name = models.CharField(max_length=20)
    def __str__(self):
        return self.level_term_name


class Designation(models.Model):
    designation_name = models.CharField(max_length=20)
    def __str__(self):
        return self.designation_name


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE) 
    post = models.CharField(max_length=1000)
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)





# class Comment(models.Model): 
#     user = models.ForeignKey(User,on_delete=models.CASCADE) 
#     post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments') 
#     parent = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE,related_name='replies') 
#     comment = models.TextField() 
    



	










@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_student:
            Student.objects.create(user = instance)
        if instance.is_teacher:
            Teacher.objects.create(user = instance)




