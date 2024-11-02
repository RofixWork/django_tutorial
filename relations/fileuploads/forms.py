from django import forms

from .models import UserData


class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ["username", "file"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "file": forms.FileInput(attrs={"class": "form-control"}),
        }
