from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Employee, AttendanceRecord

# Register your models here.
from .resources import EmployeeResource, AttendanceResource


@admin.register(Employee)
class EmployeeAdmin(ImportExportActionModelAdmin):
    resource_class = EmployeeResource


@admin.register(AttendanceRecord)
class AttendanceAdmin(ImportExportActionModelAdmin):
    resource_class = AttendanceResource
