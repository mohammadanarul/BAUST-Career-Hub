# Generated by Django 3.1.7 on 2021-05-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0006_auto_20210526_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(default='DEFAULT'),
        ),
        migrations.AddField(
            model_name='student',
            name='confirm_password',
            field=models.CharField(default='DEFAULT', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(default='DEFAULT', max_length=10),
        ),
        migrations.AddField(
            model_name='student',
            name='level_term',
            field=models.CharField(default='DEFAULT', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='DEFAULT', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(default='DEFAULT', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='picture',
            field=models.FileField(default='DEFAULT', upload_to='../Image/'),
        ),
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.CharField(default='DEFAULT', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(default='DEFAULT', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(default='DEFAULT', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(default='DEFAULT', max_length=50),
        ),
    ]
