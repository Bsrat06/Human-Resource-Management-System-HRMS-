from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'department', 'job_title', 'address', 'contact_number', 'date_of_hire', 'documents']
