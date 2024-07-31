from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.db.models import Q
from .models import AttendanceRecord, LeaveRequest, Notification
from .forms import AttendanceRecordForm, LeaveRequestForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .utils import get_notifications
from .utils import create_notification


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
    
    def test_func(self):
        allowed_groups = ['Manager', 'Admin']
        user_groups = self.request.user.groups.values_list('name', flat=True)
        return any(group in allowed_groups for group in user_groups)

    # for notifications on attendance actions
    def form_valid(self, form):
            response = super().form_valid(form)
            create_notification(self.request.user, 'Your attendance has been recorded.')
            return response
        
        
        

@login_required
def notification_list(request):
    notifications = get_notifications(request.user)
    return render(request, 'attendance/notification_list.html', {'notifications': notifications})


class AttendanceRecordUpdateView(LoginRequiredMixin, UpdateView):
    model = AttendanceRecord
    form_class = AttendanceRecordForm
    template_name = "attendance/attendance_record_form.html"
    success_url = reverse_lazy("attendance_record_list")
    
    def test_func(self):
        allowed_groups = ['Admin']
        user_groups = self.request.user.groups.values_list('name', flat=True)
        return any(group in allowed_groups for group in user_groups)
    
    # for notifications on updating attendance actions
    def form_valid(self, form):
            response = super().form_valid(form)
            create_notification(self.request.user, 'Your attendance has been updated.')
            return response


class AttendanceRecordDeleteView(LoginRequiredMixin, DeleteView):
    model = AttendanceRecord
    template_name = "attendance/attendance_record_confirm_delete.html"
    success_url = reverse_lazy("attendance_record_list")
    
    def test_func(self):
        allowed_groups = ['Admin']
        user_groups = self.request.user.groups.values_list('name', flat=True)
        return any(group in allowed_groups for group in user_groups)
    
    # for notifications on deleting attendance actions
    def form_valid(self, form):
            response = super().form_valid(form)
            create_notification(self.request.user, 'You deleted an attendance record.')
            return response


class LeaveRequestCreateView(LoginRequiredMixin, CreateView):
    model = LeaveRequest
    form_class = LeaveRequestForm
    template_name = 'attendance/leave_request_form.html'
    success_url = reverse_lazy('leave_request_list')
    
    def test_func(self):
        allowed_groups = ["Employee", "Manager", "Admin"]
        user_groups = self.request.user.groups.values_list('name', flat=True)
        return any(group in allowed_groups for group in user_groups)

    def form_valid(self, form):
        form.instance.employee = self.request.user
        response = super().form_valid(form)
        create_notification(self.request.user, 'Your leave request has been submitted.')
        return response


class LeaveRequestListView(LoginRequiredMixin, ListView):
    model = LeaveRequest
    template_name = 'attendance/leave_request_list.html'
    context_object_name = 'leave_requests'
    
    def test_func(self):
        allowed_groups = ["Employee", 'Manager', 'Admin']
        user_groups = self.request.user.groups.values_list('name', flat=True)
        return any(group in allowed_groups for group in user_groups)

    def get_queryset(self):
        return LeaveRequest.objects.filter(employee=self.request.user, status="pending")


class LeaveHistoryView(ListView):
    model = LeaveRequest
    template_name = 'attendance/leave_history.html'
    context_object_name = 'leave_requests'
    
    def test_func(self):
        allowed_groups = ["Employee", 'Manager', 'Admin']
        user_groups = self.request.user.groups.values_list('name', flat=True)
        return any(group in allowed_groups for group in user_groups)

    def get_queryset(self):
        return LeaveRequest.objects.filter(employee=self.request.user)


class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'notifications/notification_list.html'
    context_object_name = 'notifications'
    
    def test_func(self):
        allowed_groups = ["Employee", 'Manager', 'Admin']
        user_groups = self.request.user.groups.values_list('name', flat=True)
        return any(group in allowed_groups for group in user_groups)

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by('-timestamp')


# view function to mark notifications as read!
@login_required
def mark_notification_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect('notification_list')

# This is a view fucntion to mark all notifications as read at once!
@login_required
def mark_all_notifications_as_read(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    notifications.update(is_read=True)
    return redirect('notification_list')





# attendance and leave reports

def generate_attendance_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="attendance_report.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    p.setFont("Helvetica", 12)
    p.drawString(30, height - 30, "Attendance Report")
    
    attendance_records = AttendanceRecord.objects.all().order_by('employee__firstname')
    y = height - 60
    
    p.drawString(30, y, "Employee")
    p.drawString(200, y, "Date")
    p.drawString(350, y, "Status")
    y -= 20
    
    for record in attendance_records:
        p.drawString(30, y, f"{record.employee.firstname} {record.employee.last_name}")
        p.drawString(200, y, str(record.date))
        p.drawString(350, y, record.status)
        y -= 20

    p.showPage()
    p.save()
    return response


def generate_leave_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="leave_report.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    p.setFont("Helvetica", 12)
    p.drawString(30, height - 30, "Leave Report")
    
    leave_requests = LeaveRequest.objects.all().order_by('employee__firstname')
    y = height - 60
    
    p.drawString(30, y, "Employee")
    p.drawString(300, y, "Start Date")
    p.drawString(400, y, "End Date")
    p.drawString(500, y, "Status")
    y -= 20
    
    for request in leave_requests:
        p.drawString(30, y, f"{request.employee.firstname} {request.employee.last_name}")
        p.drawString(300, y, str(request.start_date))
        p.drawString(400, y, str(request.end_date))
        p.drawString(500, y, request.status)
        y -= 20

    p.showPage()
    p.save()
    return response
