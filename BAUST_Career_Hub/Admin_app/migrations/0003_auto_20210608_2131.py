# Generated by Django 3.1.7 on 2021-06-08 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0002_remove_customuser_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='profile_pic',
        ),
    ]
