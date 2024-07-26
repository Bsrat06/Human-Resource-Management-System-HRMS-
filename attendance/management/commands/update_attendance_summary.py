# attendance/management/commands/update_attendance_summary.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from attendance.models import AttendanceRecord, AttendanceSummary
from django.db.models import Count, Q
from datetime import datetime

class Command(BaseCommand):
    help = 'Updates attendance summary for all employees'

    def handle(self, *args, **kwargs):
        current_month = timezone.now().date().replace(day=1)
        summaries = []
        employees = AttendanceRecord.objects.values('employee').distinct()

        for employee in employees:
            employee_id = employee['employee']
            total_present = AttendanceRecord.objects.filter(
                employee_id=employee_id, 
                status='P', 
                date__year=current_month.year, 
                date__month=current_month.month
            ).count()
            total_absent = AttendanceRecord.objects.filter(
                employee_id=employee_id, 
                status='A', 
                date__year=current_month.year, 
                date__month=current_month.month
            ).count()

            summary, created = AttendanceSummary.objects.get_or_create(
                employee_id=employee_id, 
                month=current_month
            )
            summary.total_days_present = total_present
            summary.total_days_absent = total_absent
            summaries.append(summary)
        
        AttendanceSummary.objects.bulk_update(summaries, ['total_days_present', 'total_days_absent'])
        self.stdout.write(self.style.SUCCESS('Successfully updated attendance summary'))
