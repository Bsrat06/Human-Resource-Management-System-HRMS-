from django.urls import path
from . import views
from .views import ProfileView, ProfileEditView

urlpatterns = [
    path("", views.EmployeeListView.as_view(), name="employee_list"),
    path("employees/", views.EmployeeListView.as_view(), name="employee_list"),
    path("<int:pk>/", views.EmployeeDetailView.as_view(), name="employee_detail"),
    path("add/", views.EmployeeCreateView.as_view(), name="employee_add"),
    path("<int:pk>/edit/", views.EmployeeUpdateView.as_view(), name="employee_edit"),
    path("<int:pk>/delete/", views.EmployeeDeleteView.as_view(), name="employee_delete"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/edit/", ProfileEditView.as_view(), name="profile_edit"),
]