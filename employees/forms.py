from django import forms
from .models import Employee
from allauth.account.forms import SignupForm

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["user", "department", "job_title", "address", "contact_number", "date_of_hire", "documents"]


class CustomSignupForm(SignupForm):
    firstname = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def save(self, request):
        user = super().save(request)
        user.firstname = self.cleaned_data['firstname']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
