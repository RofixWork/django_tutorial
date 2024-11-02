import re
from datetime import datetime

from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=3,
        max_length=30,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    last_name = forms.CharField(
        min_length=3,
        max_length=30,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    date_of_birth = forms.DateField(
        help_text='format date valid like this "year-month-day"',
        widget=forms.DateInput(attrs={"class": "form-control"}),
    )
    city = forms.CharField(
        min_length=3,
        max_length=40,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Student
        fields = ["first_name", "last_name", "date_of_birth", "city"]

    def clean(self):
        data = self.cleaned_data
        date_of_birth = data.get("date_of_birth", "")

        if type(date_of_birth) == str:
            raise forms.ValidationError('format date valid like this "year-month-day"')

        year_of_birth = date_of_birth.year
        current_year = datetime.now().year
        student_age = current_year - year_of_birth

        if year_of_birth > current_year:
            raise forms.ValidationError("invalid year")

        elif student_age <= 18:
            raise forms.ValidationError("Your age must be grather than 18")
