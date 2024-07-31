from django.views.generic import ListView
from employees.models import Employee

class HomePageView(ListView):
    model = Employee
    template_name = 'home/homepage.html'
    context_object_name = 'homepage'
