from django.contrib import admin
from .models import AttendanceRecord, AttendanceSummary




class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'check_in_time', 'check_out_time', 'status')
    search_fields = ('employee__first_name', 'employee__email')
    ordering = ('employee__first_name',)
    
class AttendanceSummaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'month', 'total_days_present', 'total_days_absent')
    search_fields = ('employee__first_name', 'employee__email')
    ordering = ('employee__first_name',)

# Register your models here.
admin.site.register(AttendanceRecord, AttendanceRecordAdmin)
admin.site.register(AttendanceSummary, AttendanceSummaryAdmin)