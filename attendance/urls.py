from django.urls import path
from .views import AttendanceRecordListView, AttendanceRecordDetailView, AttendanceRecordCreateView, AttendanceRecordUpdateView, AttendanceRecordDeleteView

urlpatterns = [
    path("", AttendanceRecordListView.as_view(), name="attendance_record_list"),
    path("<int:pk>/", AttendanceRecordDetailView.as_view(), name="attendance_record_detail"),
    path("create/", AttendanceRecordCreateView.as_view(), name="attendance_record_create"),
    path("<int:pk>/edit/", AttendanceRecordUpdateView.as_view(), name="attendance_record_edit"),
    path("<int:pk>/delete/", AttendanceRecordDeleteView.as_view(), name="attendance_record_delete"),
]
