# Generated by Django 3.1.7 on 2021-08-28 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0006_auto_20210828_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin_app.department'),
        ),
    ]