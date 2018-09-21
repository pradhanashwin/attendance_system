from import_export import resources
from .models import AttendanceRecord, Employee


class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee


class AttendanceResource(resources.ModelResource):
    class Meta:
        model = AttendanceRecord


