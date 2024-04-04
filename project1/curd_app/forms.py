from django import forms

from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        widgets = {
            "emp_company_name": forms.TextInput(attrs={"class": "form-control"}),
            "emp_first_name": forms.TextInput(attrs={"class": "form-control"}),
            "emp_last_name": forms.TextInput(attrs={"class": "form-control"}),
            "emp_id": forms.NumberInput(),
            "emp_city": forms.TextInput(attrs={"class": "form-control"})
        }
