from django.contrib import admin
from .models import AttendanceRecord, AttendanceSummary


# Register your models here.

admin.site.register(AttendanceRecord)
admin.site.register(AttendanceSummary)
