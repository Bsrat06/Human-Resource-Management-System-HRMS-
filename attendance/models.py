from django.db import models
from django.conf import settings

class AttendanceRecord(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    check_in_time = models.TimeField()
    check_out_time = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[("Present", "Present"), ("Absent", "Absent")])

    def __str__(self):
        return f'{self.employee.first_name} {self.employee.last_name}  -  {self.date}  -  {self.status}'

class AttendanceSummary(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    month = models.DateField()
    total_days_present = models.IntegerField(default=0)
    total_days_absent = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.employee.first_name} {self.employee.last_name}  -  {self.month.strftime("%B %Y")}'
