from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name =models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    std_id = models.IntegerField()
    level_term = models.CharField(max_length=50,default="", editable=False)
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
    confirm_password = models.CharField(max_length=5,default="", editable=False)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    photo = models.FileField()

@receiver(post_save, sender=Admin)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()