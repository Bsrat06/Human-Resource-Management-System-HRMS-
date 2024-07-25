from django.views.generic import ListView
from employees.models import Employee

class EmployeeListView(ListView):
    model = Employee
    template_name = 'home/homepage.html'
    context_object_name = 'homepage'
