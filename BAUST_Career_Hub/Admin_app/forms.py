
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.db import transaction
from django.forms import fields
from django.forms.fields import DateField
from django.forms.models import ModelForm
from django.forms.widgets import DateInput
from . models import  CustomUser, Department, Designation, Level_Term, Student, Teacher



class StudentSignUpForm(UserCreationForm):
    department_list = []
    try:
        department = Department.objects.all()
        for dept in department:
            small_dept = (dept.id, dept.department_name)
            department_list.append(small_dept)
    except:
        department_list = []

    department = forms.ChoiceField(choices = department_list)
    

    # department_list = []
    # try:
    #     department = Department.objects.all()
    #     for dept in department:
    #         department_list.append(dept.department_name)
    # except:
    #     department_list = []


    level_term_list = []
    try:
        level_term = Level_Term.objects.all()
        for lt in level_term:
            small_lt = (lt.id, lt.level_term_name)
            level_term_list.append(small_lt)
    except:
        level_term_list = []
   
    level_term = forms.ChoiceField(choices = level_term_list)
    

    class Meta:
        
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1','password2', 'department', 'student_id', 'level_term', 'phone']

#  fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'department', 'student_id', 'level_term', 'phone']

    


class TeacherSignUpForm(UserCreationForm):
    department_list = []
    try:
        department = Department.objects.all()
        for dept in department:
            small_dept = (dept.id, dept.department_name)
            department_list.append(small_dept)
    except:
        department_list = []

    department = forms.ChoiceField(choices=department_list)
    
    designation_list = []
    try:
        designation = Designation.objects.all()
        for des in designation:
            small_des = (des.id, des.designation_name)
            designation_list.append(small_des)
    except:
        designation_list = []

    designation = forms.ChoiceField(choices = designation_list)
    

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'department', 'teacher_id', 'designation', 'phone']

  


