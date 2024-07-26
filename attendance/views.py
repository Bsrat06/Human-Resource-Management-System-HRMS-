from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.db.models import Q
from .models import AttendanceRecord
from .forms import AttendanceRecordForm


class AttendanceRecordListView(ListView):
    model = AttendanceRecord
    template_name = "attendance/attendance_record_list.html"
    context_object_name = "records"

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = AttendanceRecord.objects.all().order_by('employee__first_name')
        
        if query:
            queryset = queryset.filter(
                Q(employee__first_name__icontains=query) |
                Q(employee__email__icontains=query)
            )
        return queryset



class AttendanceRecordDetailView(DetailView):
    model = AttendanceRecord
    template_name = "attendance/attendance_record_detail.html"
    context_object_name = "record"


class AttendanceRecordCreateView(CreateView):
    model = AttendanceRecord
    form_class = AttendanceRecordForm
    template_name = "attendance/attendance_record_form.html"
    success_url = reverse_lazy("attendance_record_list")


class AttendanceRecordUpdateView(UpdateView):
    model = AttendanceRecord
    form_class = AttendanceRecordForm
    template_name = "attendance/attendance_record_form.html"
    success_url = reverse_lazy("attendance_record_list")


class AttendanceRecordDeleteView(DeleteView):
    model = AttendanceRecord
    template_name = "attendance/attendance_record_confirm_delete.html"
    success_url = reverse_lazy("attendance_record_list")
