from django.urls import path
from .views import (
    AttendanceRecordListView, 
    AttendanceRecordDetailView,
    AttendanceRecordCreateView,
    AttendanceRecordUpdateView, 
    AttendanceRecordDeleteView,
    LeaveRequestCreateView,
    LeaveRequestListView,
    LeaveHistoryView,
    generate_attendance_report,
    generate_leave_report,
    notification_list,
    mark_notification_as_read,
    NotificationListView,
    mark_all_notifications_as_read,
    )
from .views import mark_notification_as_read, NotificationListView

#app_name = 'attendance'

urlpatterns = [
    path("", AttendanceRecordListView.as_view(), name="attendance_record_list"),
    path("<int:pk>/", AttendanceRecordDetailView.as_view(), name="attendance_record_detail"),
    path("create/", AttendanceRecordCreateView.as_view(), name="attendance_record_create"),
    path("<int:pk>/edit/", AttendanceRecordUpdateView.as_view(), name="attendance_record_edit"),
    path("<int:pk>/delete/", AttendanceRecordDeleteView.as_view(), name="attendance_record_delete"),
    path('leave-request/', LeaveRequestCreateView.as_view(), name='leave_request_create'),
    path('leave-requests/', LeaveRequestListView.as_view(), name='leave_request_list'),
    path('leave-history/', LeaveHistoryView.as_view(), name='leave_history'),
        path('attendance_report/', generate_attendance_report, name='attendance_report'),
    path('leave_report/', generate_leave_report, name='leave_report'),
    path('notifications/', notification_list, name='notification_list'),
    path('notifications/', NotificationListView.as_view(), name='notification_list'),
    path('notifications/read/<int:notification_id>/', mark_notification_as_read, name='mark_notification_as_read'),
    path('notifications/read/all/', mark_all_notifications_as_read, name='mark_all_notifications_as_read'),
]