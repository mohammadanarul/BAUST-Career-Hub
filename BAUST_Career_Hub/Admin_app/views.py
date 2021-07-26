from django.contrib import auth
from django.template import RequestContext, context
from .models import CustomUser, Department, Designation, Level_Term, Student, Teacher
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .forms import  StudentSignUpForm, TeacherSignUpForm
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
    


def signup(request):
    return render(request, 'Admin_app/SignUp.html')



def student_signup(request):
    form = StudentSignUpForm()
    return render(request, 'Admin_app/StudentSignUp.html', {"form": form}) 



def teacher_signup(request):
    form = TeacherSignUpForm()
    return render(request, 'Admin_app/TeacherSignUp.html', {"form": form})



def student_signup_save(request):
    form = StudentSignUpForm()
    print(form.errors)
    if request.method == 'POST':
        print(form.errors)
        form = StudentSignUpForm(request.POST, request.FILES)
        print(form.errors)
        
        if form.is_valid():
            print(form.errors)
            instance = form.save(commit = False)
            print(form.errors)
            instance.is_student = True
            print(form.errors)
            instance.save()
            print(form.errors)
            
            return redirect('signin')

    form = StudentSignUpForm()
    print(form.errors)
    return render(request, 'Admin_app/StudentSignUp.html', {'form': form})
    


def teacher_signup_save(request):
    form = TeacherSignUpForm()

    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        
        if form.is_valid():
            instance = form.save(commit = False)
            instance.is_teacher = True
            instance.save()
            
            return redirect('signin')

    form = TeacherSignUpForm()
    return render(request, 'Admin_app/TeacherSignup.html', {'form': form})
               


                
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
    return HttpResponseRedirect("/")



@login_required  
def student_home(request):
    if request.user.is_student:
        return render(request, 'Admin_app/Student/StudentHome.html')
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



def Edit_Department(request, id):
    deptartment = Department.objects.get(id = id)
    return render(request, "Admin_app/Admin/Edit_Department.html", {"deptartment": deptartment, "id": id})



def Edit_Department_Save(request):
    if request.method == "POST":
        department_id = request.POST.get("department_id")
        department_name = request.POST.get("department_name")

        try:
            department = Department.objects.get(id=department_id)
            department.department_name = department_name
            department.save()

            messages.success(request, "Successfully Update Department")
            return HttpResponseRedirect(reverse("manage_department", kwargs={"department_id":department_id}))

        except:
            messages.error(request, "Failed to Update Department")
            return HttpResponseRedirect(reverse("edit_department", kwargs={"department_id":department_id}))
    else:
        return HttpResponse("<h2>Method not allowed</h2>")



def Add_Student(request):
    form = StudentSignUpForm()
    return render(request, 'Admin_app/Admin/Add_Student.html', {'form': form})



def Add_Student_Save(request):
    return HttpResponse('Add Student')



def Manage_Student(request):
    student = Student.objects.all()
    return render(request, "Admin_app/Admin/Manage_Student.html", {"student": student})



def Edit_Student(request):
    return HttpResponse('Edit Student')



def Edit_Student_Save(request):
    return HttpResponse('Edit Student Save')



def Add_Teacher(request):
    form = TeacherSignUpForm()
    return render(request, 'Admin_app/Admin/Add_Teacher.html', {'form': form})



def Add_Teacher_Save(request):
    return HttpResponse('Add Teacher Save')



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
    form = StudentSignUpForm()

    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        
        if form.is_valid():
            instance = form.save(commit = False)
            instance.is_student = True
            instance.save()
            
            return redirect('manage_student')

    form = StudentSignUpForm()
    return render(request, 'Admin_app/Admin/Add_Student.html', {'form': form})


def add_teacher_from_admin(request):
    form = TeacherSignUpForm()

    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        
        if form.is_valid():
            instance = form.save(commit = False)
            instance.is_teacher = True
            instance.save()
            
            return redirect('manage_teacher')

    form = TeacherSignUpForm()
    return render(request, 'Admin_app/Admin/Add_Teacher.html', {'form': form})


def student_details(request, id):
    data = Student.objects.get(id = id)
    context = {'data': data}
    return render(request, 'Admin_app/Admin/Student_details.html', context)


def student_update(request, id):
    return HttpResponse('student_update')


def student_delete(request, id):
    data = Student.objects.get(id=id)
    data.delete()
    return redirect('manage_student')


def teacher_details(request, id):
    data = Teacher.objects.get(id = id)
    context = {'data': data}
    return render(request, 'Admin_app/Admin/Teacher_details.html', context)

def teacher_update(request, id):
    return HttpResponse('teacher_update')


def teacher_delete(request, id):
    data = Teacher.objects.get(id=id)
    data.delete()
    return redirect('manage_teacher')


def department_update(request, id):
    return HttpResponse('department_update')


def department_delete(request, id):
    data = Department.objects.get(id=id)
    data.delete()
    return redirect('manage_department')


def designation_update(request, id):
    return HttpResponse('designation_update')


def designation_delete(request, id):
    data = Designation.objects.get(id=id)
    data.delete()
    return redirect('manage_designation')


def level_term_update(request, id):
    return HttpResponse('level_term_update')


def level_term_delete(request, id):
    data = Level_Term.objects.get(id=id)
    data.delete()
    return redirect('manage_level_term')
