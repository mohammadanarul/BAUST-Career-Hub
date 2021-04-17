from django.shortcuts import render

def index(request):
    return render(request, 'Admin_app/index.html')

def footer(request):
    return render(request, 'Admin_app/footer.html')

def signin(request):
    return render(request, 'Admin_app/SignIn.html')

def signup(request):
    return render(request, 'Admin_app/SignUp.html')