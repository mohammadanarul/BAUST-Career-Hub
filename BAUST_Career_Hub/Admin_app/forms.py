from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.db import transaction
from django.forms.fields import DateField
from django.forms.widgets import DateInput



class StudentSignUpForm(forms.Form):
    
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control"}))

    name = forms.CharField(label="Name", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))

    department = forms.CharField(label="Department", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))

    student_id = forms.CharField(label="Student Id", max_length=15,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    level_term = forms.CharField(label="Level Term", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))

    phone = forms.CharField(label="Phone No", max_length=15,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Password", max_length=50,
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))

    confirm_password = forms.CharField(label="Confirm Password", max_length=50,
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))
    #gender_choice = (
        ##("Male", "Male"),
        #("Female", "Female")
    #)

    #gender = forms.CharField(label="Gender", max_length=50,
                               #widget=forms.TextInput(attrs={"class": "form-control"}))
    

    
    

    #picture = forms.FileField(label="Profile Picture", widget=forms.FileInput(attrs={"class": "form-control"}))





class TeacherSignUpForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control"}))

    name = forms.CharField(label="Name", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))

    department = forms.CharField(label="Department", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))

    phone = forms.CharField(label="Phone No", max_length=15,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    
    designation = forms.CharField(label="Designation", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))

    password = forms.CharField(label="Password", max_length=50,
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))

    confirm_password = forms.CharField(label="Confirm Password", max_length=50,
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))
    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    gender = forms.ChoiceField(label="Gender", choices=gender_choice,
                               widget=forms.Select(attrs={"class": "form-control"}))

    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    

    picture = forms.ImageField(label="Profile Picture", widget=forms.FileInput(attrs={"class": "form-control"}))


