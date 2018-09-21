from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.load_home, name='load_home'),
    path('upload-attendance/', views.load_upload_attendance, name='upload_attendance'),
    path('upload-csv/', views.upload_csv, name="upload_csv"),
    path('upload-employee/', views.upload_emp_info, name='upload_employee'),
    path('all-employee-form/', views.load_all_employee_form,name='all_employee_form'),
    path('all-employee-report/', views.all_employee_report, name="all_employee_report"),
    path('specific-employee-report/', views.specific_employee_report, name="specific_employee_report"),
    path('specific-employee-analytics/<int:emp_id_id>/', views.specific_employee_analytics, name="specific_employee_analytics"),

]

