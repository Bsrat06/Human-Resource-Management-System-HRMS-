from django.urls import path
from .views import (
    AttendanceRecordListView, 
    AttendanceRecordDetailView,
    AttendanceRecordCreateView,
    AttendanceRecordUpdateView, 
    AttendanceRecordDeleteView,
    LeaveRequestCreateView,
    LeaveRequestListView,
    )

urlpatterns = [
    path("", AttendanceRecordListView.as_view(), name="attendance_record_list"),
    path("<int:pk>/", AttendanceRecordDetailView.as_view(), name="attendance_record_detail"),
    path("create/", AttendanceRecordCreateView.as_view(), name="attendance_record_create"),
    path("<int:pk>/edit/", AttendanceRecordUpdateView.as_view(), name="attendance_record_edit"),
    path("<int:pk>/delete/", AttendanceRecordDeleteView.as_view(), name="attendance_record_delete"),
    path('leave-request/', LeaveRequestCreateView.as_view(), name='leave_request_create'),
    path('leave-requests/', LeaveRequestListView.as_view(), name='leave_request_list'),
]