# attendance/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import AttendanceRecord, AttendanceSummary

@receiver(post_save, sender=AttendanceRecord)
def update_attendance_summary(sender, instance, **kwargs):
    employee = instance.employee
    current_month = instance.date.replace(day=1)
    
    total_present = AttendanceRecord.objects.filter(
        employee=employee, 
        status='P', 
        date__year=current_month.year, 
        date__month=current_month.month
    ).count()
    total_absent = AttendanceRecord.objects.filter(
        employee=employee, 
        status='A', 
        date__year=current_month.year, 
        date__month=current_month.month
    ).count()

    summary, created = AttendanceSummary.objects.get_or_create(
        employee=employee, 
        month=current_month
    )
    summary.total_days_present = total_present
    summary.total_days_absent = total_absent
    summary.save()
