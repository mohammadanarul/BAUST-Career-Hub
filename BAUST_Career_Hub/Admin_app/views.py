from django.contrib import auth
from django.template import RequestContext, context
from .models import CustomUser, Department, Designation, Level_Term, Post, Student, Teacher
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, response
from django.contrib import messages
from django.urls import reverse
from .forms import   UserCreateForm,StudentAddForm, TeacherAddForm
from django.contrib.auth import login, authenticate, logout
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.template import RequestContext
from django.contrib.auth.decorators import login_required






def index(request):
    return render(request, 'Admin_app/index.html')



def footer(request):
    return render(request, 'Admin_app/footer.html')



def signin(request):
    # form = AuthenticationForm()
    return render(request, 'Admin_app/Login.html')



def student_signup(request):
    user_form = UserCreateForm()
    student_form = StudentAddForm()
    return render(request, 'Admin_app/StudentSignUp.html', {"user_form": user_form, "student_form": student_form}) 


def teacher_signup(request):
    user_form = UserCreateForm()
    teacher_form = TeacherAddForm()
    return render(request, 'Admin_app/TeacherSignUp.html', {"user_form": user_form, "teacher_form": teacher_form})



def student_signup_save(request):
    user_form = UserCreateForm()
    student_form = StudentAddForm()

    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
        student_form = StudentAddForm(request.POST)
        
        if user_form.is_valid() and student_form.is_valid():
            user_obj = user_form.save()
            student_obj = student_form.save(commit = False)
            student_obj.user = user_obj
            student_obj.save()
            return redirect('signin')
        else:
            return render(request, 'Admin_app/StudentSignUp.html', {'user_form': user_form,'student_form':student_form})
        
        
    return render(request, 'Admin_app/StudentSignUp.html', {'user_form': user_form,'student_form':student_form})
    


def teacher_signup_save(request):
    user_form = UserCreateForm()
    teacher_form = TeacherAddForm()

    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
        teacher_form = TeacherAddForm(request.POST)
        
        if user_form.is_valid() and teacher_form.is_valid():
            user_obj = user_form.save()
            teacher_obj = teacher_form.save(commit = False)
            teacher_obj.user = user_obj
            teacher_obj.save()
            return redirect('signin')
        else:
            return render(request, 'Admin_app/TeacherSignUp.html', {'user_form': user_form,'teacher_form':teacher_form})
        
        
    return render(request, 'Admin_app/TeacherSignUp.html', {'user_form': user_form,'teacher_form':teacher_form})
               


                
   #with user type
def user_signin(request):
    username_err = ''
    password_err = ''
    inactivity = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password = password)
        password_check = CustomUser.objects.filter(password__iexact = password).exists()
        uername_check = CustomUser.objects.filter(username__iexact = username).exists()
        if not uername_check:
            username_err = 'This username does not match our records'

        elif not password_check:
            password_err = 'You entered a wrong password'

        if user:
            if user.is_active == False:
                inactivity = 'This account is not active'
            else:
                login(request,user)
                if user.is_student:
                    return redirect('student_home')
                elif user.is_teacher:
                    return redirect('teacher_home')
                elif user.is_superuser:
                    return redirect('admin_home')

    context = {
        'username_err': username_err,
        'password_err': password_err,
        'inactive': inactivity,
    }
    return render(request, "Admin_app/Login.html", context)



def user_logout(request):
    logout(request)
    return HttpResponseRedirect("signin")



@login_required  
def student_home(request):
    if request.user.is_student:
        data = Student.objects.get()
        posts = Post.objects.get()

        
        return render(request, 'Admin_app/Student/StudentHome.html', {'data': data, 'posts': posts})
        # return render(request, 'Admin_app/Student/StudentHome.html')
    else:
        return HttpResponse('You are not as Student!')



@login_required
def admin_home(request):
    if request.user.is_superuser:
        return render(request, 'Admin_app/Admin/AdminHome.html')
    else:
        return HttpResponse('You are not as Admin!')



@login_required
def teacher_home(request):
    if request.user.is_teacher:
       
        return render(request, 'Admin_app/TeacherHome.html')
    else:
        return HttpResponse('You are not as Teacher!')



def Add_Department(request):
    return render(request, 'Admin_app/Admin/Add_Department.html')



def Add_Department_Save(request):
    if request.method == "POST":
        department = request.POST.get("department_name")

        try:
            dept_model = Department(department_name=department)
            dept_model.save()
            messages.success(request, "Successfully Added Department")
            return HttpResponseRedirect(reverse("manage_department"))
        except:
            messages.error(request, "Failed to Add Department")
            return HttpResponseRedirect(reverse("add_department"))
    
    else:
        return HttpResponse("Method not allowed")



def Manage_Department(request):
    department = Department.objects.all()
    return render(request, "Admin_app/Admin/Manage_Department.html", {"department": department})



# def Add_Student(request):
#     # form = StudentSignUpForm()
#     # return render(request, 'Admin_app/Admin/Add_Student.html', {'form': form})



def Add_Student_Save(request):
    return HttpResponse('Add Student')



def Manage_Student(request):
    student = Student.objects.all()
    return render(request, "Admin_app/Admin/Manage_Student.html", {"student": student})




def Manage_Teacher(request):
    teacher = Teacher.objects.all()
    return render(request, "Admin_app/Admin/Manage_Teacher.html", {"teacher": teacher})



def Edit_Teacher(request):
    return HttpResponse('Edit Teacher')



def Edit_Teacher_Save(request):
    return HttpResponse('Edit Teacher Save')



def Add_Designation(request):
    return render(request, 'Admin_app/Admin/Add_Designation.html')



def Add_Designation_Save(request):
    if request.method == "POST":
        designation = request.POST.get("designation_name")
        try:
            designation_model = Designation(designation_name=designation)
            designation_model.save()
            messages.success(request, "Successfully Added Designation")
            return HttpResponseRedirect(reverse("manage_designation"))
        except:
            messages.error(request, "Failed to Add Designation")
            return HttpResponseRedirect(reverse("add_designation"))
    
    else:
        return HttpResponse("Method not allowed")



def Manage_Designation(request):
    designation = Designation.objects.all()
    return render(request, "Admin_app/Admin/Manage_Designation.html", {"designation": designation})



def Edit_Designation(request):
    return HttpResponse('Edit Student')



def Edit_Designation_Save(request):
    return HttpResponse('Edit Student Save')



def Add_Level_Term(request):
    return render(request, 'Admin_app/Admin/Add_Level_Term.html')



def Add_Level_Term_Save(request):
    if request.method == "POST":
        level_term_name = request.POST.get("level_term_name")

        try:
            level_term_model = Level_Term(level_term_name=level_term_name)
            level_term_model.save()
            messages.success(request, "Successfully Added Level-Term")
            return HttpResponseRedirect(reverse("manage_level_term"))
        except:
            messages.error(request, "Failed to Add Level-Term")
            return HttpResponseRedirect(reverse("add_level_term"))
    
    else:
        return HttpResponse("Method not allowed")



def Manage_Level_Term(request):
    level_term = Level_Term.objects.all()
    return render(request, "Admin_app/Admin/Manage_Level_term.html", {"level_term": level_term})



def Edit_Level_Term(request):
    return HttpResponse('Edit Student')



def Edit_Level_Term_Save(request):
    return HttpResponse('Edit Student Save')


def add_student_from_admin(request):
    user_form = UserCreateForm()
    student_form = StudentAddForm()

    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
        student_form = StudentAddForm(request.POST)
        
        if user_form.is_valid() and student_form.is_valid():
            user_obj = user_form.save()
            student_obj = student_form.save(commit = False)
            student_obj.user = user_obj
            student_obj.save()
            return redirect('manage_student')
        else:
            return render(request, 'Admin_app/Admin/Add_Student.html', {'user_form': user_form,'student_form':student_form})
        
        
    return render(request, 'Admin_app/Admin/Add_Student.html', {'user_form': user_form,'student_form':student_form})
            
            

    


def add_teacher_from_admin(request):
    user_form = UserCreateForm()
    teacher_form = TeacherAddForm()

    if request.method == 'POST':
        user_form = UserCreateForm(request.POST)
        teacher_form = TeacherAddForm(request.POST)
        
        if user_form.is_valid() and teacher_form.is_valid():
            user_obj = user_form.save()
            teacher_obj = teacher_form.save(commit = False)
            teacher_obj.user = user_obj
            teacher_obj.save()
            return redirect('manage_teacher')
        else:
            return render(request, 'Admin_app/Admin/Add_Teacher.html', {'user_form': user_form,'teacher_form':teacher_form})
        
        
    return render(request, 'Admin_app/Admin/Add_Teacher.html', {'user_form': user_form,'teacher_form':teacher_form})


def student_details(request, id):
    data = Student.objects.get(id = id)
    context = {'data': data}
    return render(request, 'Admin_app/Admin/Student_details.html', context)


def student_update(request, id):
    user_form = UserCreateForm()
    student_form = StudentAddForm()
    student = Student.objects.get(id = id)
    return render(request, 'Admin_app/Admin/Update_student.html', {'user_form':user_form, 'student_form':student_form, 'student':student})

def student_update_save(request):
    pass
    # user = CustomUser.objects.get(id=id)
    # student = Student.objects.get(id = id)
    # user_form = UserCreateForm(request.POST or None, instance = user.user)
    # student_form = StudentAddForm(request.POST or None, instance = student.user)
    
    # if user_form.is_valid() and student_form.is_valid():
    #     # form = form.save(commit=False)
    #     # form.save()
    #     user_obj = user_form.save()
    #     student_obj = student_form.save(commit = False)
    #     student_obj.user = user_obj
    #     student_obj.save()
    #     return redirect('manage_student')
        
    # else:
    #     return render(request, 'Admin_app/Admin/Add_Student.html', {'user_form': user_form,'student_form':student_form})
        


def student_delete(request, id):
    data = Student.objects.get(id=id)
    data.delete()
    return redirect('manage_student')


def teacher_details(request, id):
    data = Teacher.objects.get(id = id)
    context = {'data': data}
    return render(request, 'Admin_app/Admin/Teacher_details.html', context)

def teacher_update(request, id):
    user_form = UserCreateForm()
    teacher_form = TeacherAddForm()
    teacher = Teacher.objects.get(id = id)
    return render(request, 'Admin_app/Admin/Update_Teacher.html', {'user_form':user_form, 'teacher_form':teacher_form, 'teacher':teacher})

def teacher_update_save():
    pass


def teacher_delete(request, id):
    data = Teacher.objects.get(id=id)
    data.delete()
    return redirect('manage_teacher')


def department_update(request, id):
    # return HttpResponse('department_update')
    # dept = Department.objects.get()
    
    return render(request, 'Admin_app/Admin/Update_Department.html')
    

def update_department_save(request):
    pass
    

    


def department_delete(request, id):
    data = Department.objects.get(id=id)
    data.delete()
    return redirect('manage_department')


def designation_update(request, id):
    return render(request, 'Admin_app/Admin/Update_Designation.html')

def update_designation_save(request):
    pass


def designation_delete(request, id):
    data = Designation.objects.get(id=id)
    data.delete()
    return redirect('manage_designation')


def level_term_update(request, id):
    return render(request, 'Admin_app/Admin/Update_Level_Term.html')
    # return HttpResponse('level_term_update')

def update_level_term_save(request):
    pass


def level_term_delete(request, id):
    data = Level_Term.objects.get(id=id)
    data.delete()
    return redirect('manage_level_term')

def student_profile(request):
    data = Student.objects.get()
    return render(request,'Admin_app/Student/student_profile.html', {'data': data})

def student_post(request):
    if request.method == "POST":
        post = request.POST.get("post")

        try:
            post_model = Post(post=post)
            post_model.save()
            messages.success(request, "Successfully Added Department")
            return HttpResponseRedirect(reverse("student_home"))
        except:
            messages.error(request, "Failed to Add Department")
            return HttpResponseRedirect(reverse("student_home"))
    
    else:
        return HttpResponse("Method not allowed")