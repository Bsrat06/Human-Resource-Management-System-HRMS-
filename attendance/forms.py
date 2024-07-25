# attendance/forms.py
from django import forms
from .models import AttendanceRecord

class AttendanceRecordForm(forms.ModelForm):
    class Meta:
        model = AttendanceRecord
        fields = ['employee', 'date', 'check_in_time', 'check_out_time', 'status']
