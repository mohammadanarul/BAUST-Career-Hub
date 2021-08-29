# Generated by Django 3.1.7 on 2021-08-28 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0008_auto_20210828_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='level_term',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='teacher_id',
        ),
        migrations.AddField(
            model_name='student',
            name='level_term',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin_app.level_term'),
        ),
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='designation',
            field=models.CharField(default='sdsd', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_id',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
