from django.db import models
from django.conf import settings
from django.db import models

class AttendanceRecord(models.Model):
    STATUS_CHOICES= [
        ("P", "Present"),
        ("A", "Absent")
    ]
    
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    check_in_time = models.TimeField()
    check_out_time = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.employee.first_name} {self.employee.last_name}  -  {self.date}  -  {self.status}'

class AttendanceSummary(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    month = models.DateField()
    total_days_present = models.IntegerField(default=0)
    total_days_absent = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.employee.first_name} {self.employee.last_name}  -  {self.month.strftime("%B %Y")}'
