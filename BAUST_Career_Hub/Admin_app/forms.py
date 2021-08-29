
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.db import transaction
from django.forms import fields
from django.forms.fields import DateField
from django.forms.models import ModelForm
from django.forms.widgets import DateInput
from . models import  CustomUser, Department, Designation, Level_Term, Student, Teacher



class UserCreateForm(UserCreationForm): 

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1','password2', 'department', 'phone']

#  fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'department', 'student_id', 'level_term', 'phone']

class StudentAddForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user']


class TeacherAddForm(forms.ModelForm):
    class  Meta:
        model = Teacher
        exclude = ['user']

  


