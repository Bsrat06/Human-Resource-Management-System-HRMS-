from django.urls import path ,include
from . import views

urlpatterns = [
    path("login", views.login_user, name="login"), 
    path("emp_login", views.emp_login, name="emp_login"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("home", views.hr, name="benefit"),
    path("plans/enroll/<str:eid>", views.enroll,name="enroll"),
    path("benefit", views.index,name="emp_benefit"),
    path("notif", views.notif),
    path("request/", views.request),
    path("plan/", views.plan),
    path("plans/<str:eid>", views.plans),
    path("myenrol/<str:eid>", views.myenroll),
    path("add/", views.add),
    path("sum/", views.sum),
    
    
]
