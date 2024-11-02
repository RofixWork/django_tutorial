import re

from django import forms
from django.core import validators

from .models import Teacher


# create first form
class TeacherForm(forms.ModelForm):
    name = forms.CharField(
        validators=[
            validators.RegexValidator(
                r"^([A-Z][a-z]+)\s([A-Z][a-z]+)$",
                message="Please enter your name in the format: 'FirstName LastName'. Each name must start with an uppercase letter followed by lowercase letters.",
            ),
        ],
        widget=forms.TextInput(attrs={"class": "form-control", "id": "input_name"}),
        label="Your Name",
    )

    class Meta:
        model = Teacher
        fields = "__all__"
        # exclude = ["email"]
        labels = {
            "name": "Your Name",
            "email": "Your Email",
            "phone_number": "Contact Number",
        }
        widgets = {
            "email": forms.EmailInput(
                attrs={"class": "form-control", "id": "input_email"}
            ),
            "phone_number": forms.TextInput(
                attrs={"class": "form-control", "id": "input_phone_number"}
            ),
        }
        help_texts = {"email": "we accept only gmail emails"}
        error_messages = {"name": {"required": "name field is required..."}}

    # name = forms.CharField(
    #     min_length=5,
    #     label="Your Name",
    #     label_suffix="",
    #     error_messages={"required": "your name field cannot be empty"},
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control", "id": "exampleInputEmail1"}
    #     ),
    #     validators=[
    #         validators.MaxLengthValidator(15),
    #         validators.RegexValidator(
    #             r"^([A-Z][a-z]+)\s([A-Z][a-z]+)$",
    #             message="Please enter your name in the format: 'FirstName LastName'. Each name must start with an uppercase letter followed by lowercase letters.",
    #         ),
    #     ],
    # )
    # email = forms.EmailField(
    #     label="Your Email",
    #     label_suffix="",
    #     help_text="we only accpet email from gmail.com",
    #     widget=forms.EmailInput(
    #         attrs={"class": "form-control", "id": "exampleInputEmail2"}
    #     ),
    #     # validators=[validators.EmailValidator("invalid email format")],
    # )
    # phone_number = forms.CharField(
    #     label="Contact Number",
    #     label_suffix="",
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control", "id": "exampleInputEmail3"}
    #     ),
    #     validators=[
    #         validators.RegexValidator(
    #             r"^(\+212|0)(6|7)([0-9]{8})$",
    #             message="Invalid phone number format. Please enter a valid Moroccan phone number that starts with +212 or 0, followed by 6 or 7, and exactly 8 digits.",
    #         )
    #     ],
    # )
    # bio = forms.CharField(
    #     widget=forms.Textarea(attrs={"cols": 10, "class": "bio_content"})
    # )

    # def clean(self):
    #     # cleaned_data = super().clean()
    #     name = self.cleaned_data["name"]
    #     phone_number = self.cleaned_data["phone_number"]
    #     if not re.match(r"^([A-Z][a-z]+)\s([A-Z][a-z]+)$", name):
    #         raise forms.ValidationError(
    #             "Please enter your name in the format: 'FirstName LastName'. Each name must start with an uppercase letter followed by lowercase letters."
    #         )

    #     if not re.match(r"^(\+212|0)(6|7)([0-9]{8})$", phone_number):
    #         raise forms.ValidationError(
    #             "Invalid phone number format. Please enter a valid Moroccan phone number that starts with +212 or 0, followed by 6 or 7, and exactly 8 digits."
    #         )
