
from .models import Student, Teacher
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .forms import StudentSignUpForm, TeacherSignUpForm
from django.contrib.auth import login, authenticate
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404

from django.template import RequestContext
def index(request):
    return render(request, 'Admin_app/index.html')



def footer(request):
    return render(request, 'Admin_app/footer.html')



def signin(request):
    return render(request, 'Admin_app/SignIn.html')



def signup(request):
    return render(request, 'Admin_app/SignUp.html')



def student_signup(request):
    form = StudentSignUpForm()
    return render(request, 'Admin_app/StudentSignUp.html', {"form": form}) 



def teacher_signup(request):
    form = TeacherSignUpForm()
    return render(request, 'Admin_app/TeacherSignUp.html', {"form": form})



def student_signup_save(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            department = form.cleaned_data['department']
            student_id = form.cleaned_data['student_id']
            level_term = form.cleaned_data['level_term']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            #gender = form.cleaned_data['gender']
            #dob = form.cleaned_data['dob']
            #address = form.cleaned_data['address']
            #picture = form.cleaned_data['picture']

            try:
                user = Student()
                
                user.email = email
                user.name = name
                user.department = department
                user.student_id = student_id
                user.level_term = level_term
                user.phone = phone
                user.password = password
                user.confirm_password = confirm_password
                #user.gender - gender
                #user.dob = dob
                #user.address = address
                #user.picture = picture


                user.save()
                messages.success(request, "Registration successfully")              
                return HttpResponseRedirect(reverse("signin"))
               

            except:
                messages.error(request, "Registration Failed!!")              
                return HttpResponseRedirect(reverse("student_signup"))
                

    else:
        form = StudentSignUpForm()
    return render(request, 'Admin_app/StudentSignUp.html', {'form': form})




def teacher_signup_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        form = TeacherSignUpForm(request.POST, request.FILES)

        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            department = form.cleaned_data['department']
            phone = form.cleaned_data['phone']
            designation = form.cleaned_data['designation']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            gender = form.cleaned_data['gender']
            address = form.cleaned_data['address']
            
            picture = request.FILES['picture']
            fs = FileSystemStorage()
            filename = fs.save(picture.name, picture)
            profile_pic_url = fs.url(filename)

            try:
                user = Teacher.objects.create_user(password=password,confirm_password=confirm_password, email=email,name=name,  user_type=2)
                user.student.department = department
                user.student.phone = phone
                user.student.designation = designation
                user.student.gender = gender
                user.student.address = address
                
                user.student.picture = profile_pic_url
                
                user.save()
                
                messages.success(request, "Registration successfully")
                
                return HttpResponseRedirect(reverse("signin"))
               

            except:
                
                messages.error(request, "Registration Failed!!")
                
                return HttpResponseRedirect(reverse("teacher_signup"))
                

        else:
            form = StudentSignUpForm(request.POST)
            return render(request, 'Admin_app/TeacherSignUp.html', {"form": form})


