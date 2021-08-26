from os import name
from django.contrib import admin
from django.contrib.auth import login
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = "index"),

    path('signin', views.signin, name = "signin"),
    path('signup', views.signup, name = "signup"),


    path('student_signup', views.student_signup, name = "student_signup"),
    path('student_signup_save', views.student_signup_save, name = "student_signup_save"),


    path('teacher_signup', views.teacher_signup, name = "teacher_signup"),
    path('teacher_signup_save', views.teacher_signup_save, name = "teacher_signup_save"),


    path('user_signin', views.user_signin, name = "user_signin"),
    path('user_logout', views.user_logout,  name = "user_logout"),


    path('student_home', views.student_home, name = "student_home"),

    
    path('teacher_home', views.teacher_home, name = "teacher_home"),


    path('admin_home', views.admin_home, name = "admin_home"),

    path('add_student', views.Add_Student, name = "add_student"),
    path('add_student_save', views.Add_Student_Save, name = "add_student_save"),
    path('manage_student', views.Manage_Student, name = "manage_student"),
    # path('edit_student', views.Edit_Student, name = "edit_student"),

    # path('student_update_save', views.student_update_save, name = "student_update_save"),

    path('add_teacher', views.Add_Teacher, name = "add_teacher"),
    path('add_teacher_save', views.Add_Teacher_Save, name = "add_teacher_save"),
    path('manage_teacher', views.Manage_Teacher, name = "manage_teacher"),
    path('edit_teacher', views.Edit_Teacher, name = "edit_teacher"),
    path('edit_teacher_save', views.Edit_Teacher_Save, name = "edit_teacher_save"),

    path('add_department', views.Add_Department, name = "add_department"),
    path('add_department_save', views.Add_Department_Save, name = "add_department_save"),
    path('manage_department', views.Manage_Department, name = "manage_department"),
    path('edit_department/<int:id>', views.Edit_Department, name = "edit_department"),
    path('edit_department_save', views.Edit_Department_Save, name = "edit_department_save"),
    
    path('add_designation', views.Add_Designation, name = "add_designation"),
    path('add_designation_save', views.Add_Designation_Save, name = "add_designation_save"),
    path('manage_designation', views.Manage_Designation, name = "manage_designation"),
    path('edit_designation/<int:id>', views.Edit_Designation, name = "edit_designation"),
    path('edit_designation_save', views.Edit_Designation_Save, name = "edit_designation_save"),

    path('add_level_term', views.Add_Level_Term, name = "add_level_term"),
    path('add_level_term_save', views.Add_Level_Term_Save, name = "add_level_term_save"),
    path('manage_level_term', views.Manage_Level_Term, name = "manage_level_term"),
    path('edit_level_term/<int:id>', views.Edit_Level_Term, name = "edit_level_term"),
    path('edit_level_term_save', views.Edit_Level_Term_Save, name = "edit_level_term_save"),

    path('add_student_from_admin', views.add_student_from_admin, name="add_student_from_admin"),
    path('add_teacher_from_admin', views.add_teacher_from_admin, name="add_teacher_from_admin"),

    path('student_details/<int:id>/', views.student_details, name="student_details"),
    path('student_update/<int:id>/', views.student_update, name="student_update"),
    path('student_delete/<int:id>/', views.student_delete, name="student_delete"),

    path('teacher_details/<int:id>/', views.teacher_details, name="teacher_details"),
    path('teacher_update/<int:id>/', views.teacher_update, name="teacher_update"),
    path('teacher_delete/<int:id>/', views.teacher_delete, name="teacher_delete"),

    path('department_update/<int:id>/', views.department_update, name="department_update"),
    path('department_delete/<int:id>/', views.department_delete, name="department_delete"),

    path('designation_update/<int:id>/', views.designation_update, name="designation_update"),
    path('designation_delete/<int:id>/', views.designation_delete, name="designation_delete"),

    path('level_term_update/<int:id>/', views.level_term_update, name="level_term_update"),
    path('level_term_delete/<int:id>/', views.level_term_delete, name="level_term_delete"),

    path('student_profile', views.student_profile, name="student_profile"),
    



    
]