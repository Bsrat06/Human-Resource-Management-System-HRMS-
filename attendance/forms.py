# attendance/forms.py
from django import forms
from .models import AttendanceRecord
from .models import LeaveRequest

class AttendanceRecordForm(forms.ModelForm):
    class Meta:
        model = AttendanceRecord
        fields = ["employee", "date", "check_in_time", "check_out_time", "status"]


class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['start_date', 'end_date', 'reason']
