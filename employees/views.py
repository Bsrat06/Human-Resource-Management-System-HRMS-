from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Employee, Notification
from .forms import EmployeeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from attendance.utils import create_notification
from attendance.views import NotificationListView, notification_list, mark_notification_as_read, mark_all_notifications_as_read


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = "employees/employee_list.html"
    context_object_name = "employees"
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Employee.objects.filter(
                Q(employee__firstname__icontains=query)
                | Q(employee__email__icontains=query)
            )
        return super().get_queryset()

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = "employees/employee_detail.html"
    context_object_name = "employee"

class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "employees/employee_form.html"
    success_url = reverse_lazy("employee_list")
    
    # for notifications on creating new employee
    def form_valid(self, form):
            response = super().form_valid(form)
            create_notification(self.request.user, 'You created an employee record.')
            return response

class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "employees/employee_form.html"
    success_url = reverse_lazy("employee_list")
    
    # for notifications on updating employee informationS
    def form_valid(self, form):
            response = super().form_valid(form)
            create_notification(self.request.user, 'You updated an employee record.')
            return response

class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    template_name = "employees/employee_confirm_delete.html"
    success_url = reverse_lazy("employee_list")
    
    # for notifications on deleting an employee actions
    def form_valid(self, form):
            response = super().form_valid(form)
            create_notification(self.request.user, 'You deleted an employee record.')
            return response