from django import forms
from dashboard.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee

        fields = [
            "personnel_code",
            "first_name",
            "last_name",
            "national_code",
            "mobile",
            "department",
            "job_title",
            "hire_date",
            "is_active",
        ]

        widgets = {
            "hire_date": forms.DateInput(attrs={"type": "date"}),
        }