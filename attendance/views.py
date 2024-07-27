from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.db.models import Q
from .models import AttendanceRecord, LeaveRequest
from .forms import AttendanceRecordForm, LeaveRequestForm
from django.contrib.auth.mixins import LoginRequiredMixin


class AttendanceRecordListView(LoginRequiredMixin, ListView):
    model = AttendanceRecord
    template_name = "attendance/attendance_record_list.html"
    context_object_name = "records"

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = AttendanceRecord.objects.all().order_by('employee__firstname')
        
        if query:
            queryset = queryset.filter(
                Q(employee__firstname__icontains=query) |
                Q(employee__email__icontains=query)
            )
        return queryset



class AttendanceRecordDetailView(LoginRequiredMixin, DetailView):
    model = AttendanceRecord
    template_name = "attendance/attendance_record_detail.html"
    context_object_name = "record"


class AttendanceRecordCreateView(LoginRequiredMixin, CreateView):
    model = AttendanceRecord
    form_class = AttendanceRecordForm
    template_name = "attendance/attendance_record_form.html"
    success_url = reverse_lazy("attendance_record_list")


class AttendanceRecordUpdateView(LoginRequiredMixin, UpdateView):
    model = AttendanceRecord
    form_class = AttendanceRecordForm
    template_name = "attendance/attendance_record_form.html"
    success_url = reverse_lazy("attendance_record_list")


class AttendanceRecordDeleteView(LoginRequiredMixin, DeleteView):
    model = AttendanceRecord
    template_name = "attendance/attendance_record_confirm_delete.html"
    success_url = reverse_lazy("attendance_record_list")


class LeaveRequestCreateView(LoginRequiredMixin, CreateView):
    model = LeaveRequest
    form_class = LeaveRequestForm
    template_name = 'attendance/leave_request_form.html'
    success_url = reverse_lazy('leave_request_list')

    def form_valid(self, form):
        form.instance.employee = self.request.user
        return super().form_valid(form)

class LeaveRequestListView(LoginRequiredMixin, ListView):
    model = LeaveRequest
    template_name = 'attendance/leave_request_list.html'
    context_object_name = 'leave_requests'

    def get_queryset(self):
        return LeaveRequest.objects.filter(employee=self.request.user, status="pending")


class LeaveHistoryView(ListView):
    model = LeaveRequest
    template_name = 'attendance/leave_history.html'
    context_object_name = 'leave_requests'

    def get_queryset(self):
        return LeaveRequest.objects.filter(employee=self.request.user)

