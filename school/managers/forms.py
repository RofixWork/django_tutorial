from django import forms
from django.core import validators


class ManagerForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "id": "input_name"}),
        label="Your Name",
        validators=[
            validators.RegexValidator(
                r"^[a-z]+\s[a-z]+$",
                message="Please enter a valid full name with two words, all in lowercase letters and separated by a space.",
            ),
            validators.MaxLengthValidator(100),
            validators.MinLengthValidator(6),
        ],
    )
    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={"class": "form-control", "id": "input_phone_number"}
        ),
        label="Phone Number",
        validators=[
            validators.RegexValidator(
                r"^(\+212|0)(6|7)([0-9]{8})$",
                message="Invalid phone number format. Please enter a valid Moroccan phone number that starts with +212 or 0, followed by 6 or 7, and exactly 8 digits.",
            )
        ],
    )
    hire_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"class": "form-control", "id": "input_hire_date"}
        ),
        label="Hire Date",
    )
    department = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "input_dept"}),
        label="Department",
    )
    salary = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=1000,
        widget=forms.NumberInput(attrs={"class": "form-control", "id": "input_salary"}),
        label="Salary",
    )
