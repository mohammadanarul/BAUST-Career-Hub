from django import forms

class DateInput(forms.DateInput):
    input_type = "date"


class AdminSignUpForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control"}))

    name = forms.CharField(label="Full Name", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))

    phone = forms.CharField(label="Phone No", max_length=50,
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

    profile_pic = forms.FileField(label="Profile Image", widget=forms.FileInput(attrs={"class": "form-control"}))