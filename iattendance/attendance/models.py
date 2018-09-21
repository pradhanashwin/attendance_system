from django.db import models


class Employee(models.Model):
    class Meta:
        db_table = 'Employee'

    emp_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True,default=1)
    position = models.CharField(max_length=100, blank=True, null=True,default='Developer')

    def __str__(self):
        return self.name


class AttendanceRecord(models.Model):
    class Meta:
        db_table = 'AttendanceRecord'
    #emp_id is returned as a employee objec
    #to get employee id we mus  type emp_id_id------Ref. bishal
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
   # emp_id = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=100, blank=True, null=True)
    miti = models.CharField(max_length=100, blank=True, null=True)
    day = models.CharField(max_length=100, blank=True, null=True)
    in_time = models.CharField(max_length=100, blank=True, null=True)
    out_time = models.CharField(max_length=100, blank=True, null=True)
    punch_count = models.IntegerField(blank=True, null=True)
    difference_time = models.FloatField(blank=True, null=True)
    time_spent = models.FloatField(blank=True, null=True)


    def __str__(self):
        return self.emp_id.name

class Department:
    class Meta:
        db_table = 'Department'

    department_id = models.IntegerField(primary_key=True)
    staff_count= models.IntegerField()







