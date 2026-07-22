from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee

        fields = [
            "personnel_code",
            "first_name",
            "last_name",
            "national_code",
            "phone",
            "unit",
            "employment_type",
            "is_active",
        ]

        widgets = {

            "personnel_code": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "کد پرسنلی را وارد کنید"
            }),

            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "نام"
            }),

            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "نام خانوادگی"
            }),

            "national_code": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "کد ملی"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "شماره تماس"
            }),

            "unit": forms.Select(attrs={
                "class": "form-select"
            }),

            "employment_type": forms.Select(attrs={
                "class": "form-select"
            }),

            "is_active": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),

        }