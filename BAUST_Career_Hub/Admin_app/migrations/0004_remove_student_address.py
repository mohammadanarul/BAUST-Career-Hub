# Generated by Django 3.1.7 on 2021-05-23 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0003_auto_20210523_2220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
    ]