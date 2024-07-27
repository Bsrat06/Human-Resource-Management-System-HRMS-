from django.contrib import admin
from .models import AttendanceRecord, AttendanceSummary, LeaveRequest




class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'check_in_time', 'check_out_time', 'status')
    search_fields = ('employee__firstname', 'employee__email')
    ordering = ('employee__firstname',)
    
class AttendanceSummaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'month', 'total_days_present', 'total_days_absent')
    search_fields = ('employee__firstname', 'employee__email')
    ordering = ('employee__firstname',)

# Register your models here.
admin.site.register(AttendanceRecord, AttendanceRecordAdmin)
admin.site.register(AttendanceSummary, AttendanceSummaryAdmin)
admin.site.register(LeaveRequest)