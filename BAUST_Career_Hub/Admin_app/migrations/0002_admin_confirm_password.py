# Generated by Django 3.1.7 on 2021-04-23 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='confirm_password',
            field=models.CharField(default='', editable=False, max_length=50),
        ),
    ]
