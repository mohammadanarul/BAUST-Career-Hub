from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from Admin_app.models import Admin
from Admin_app.forms import AdminSignUpForm
from django.contrib.auth import login, authenticate
from django.core.files.storage import FileSystemStorage


def index(request):
    return render(request, 'Admin_app/index.html')

def footer(request):
    return render(request, 'Admin_app/footer.html')

def signin(request):
    return render(request, 'Admin_app/SignIn.html')

def signup(request):
    return render(request, 'Admin_app/SignUp.html')

def base(request):
    return render(request, 'Admin_app/base_template.html')

def doSignUp(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        form = AdminSignUpForm(request.POST, request.FILES)

        if form.is_valid():
            
            email = form.cleaned_data["email"]
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]
            gender = form.cleaned_data["gender"]
            address = form.cleaned_data["address"]
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)

            try:
                user = authenticate( email=email,password=password,name=name,)
                user.Admin.phone = phone
                user.Admin.gender = gender
                user.Admin.address = address
                user.Admin.profile_pic = profile_pic_url
                user.save()
                messages.success(request, "Waiting for Admin Approval....")
                return HttpResponseRedirect(reverse("signin"))

            except:
                messages.error(request, "Failed, Try Agian!!")
                return HttpResponseRedirect(reverse("signup"))

        else:
            form = AdminSignUpForm(request.POST)
            return render(request, "Admin_app/SignUp.html", {"form": form})



