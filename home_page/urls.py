from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='homepage'),
    path('employees/', views.EmployeeListView.as_view(), name='employees'),
]
