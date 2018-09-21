from django import forms

from .models import Employee, AttendanceRecord


class UploadFileForm(forms.Form):
    file = forms.FileField()


class UploadEmpInfo(forms.ModelForm):
    # emp_id = forms.IntegerField()
    # name = forms.CharField(max_length=100)
    # department_id= forms.IntegerField()
    # position=forms.CharField(max_length=100)
    class Meta:
        model=Employee
        fields=['emp_id','name','department_id','position']


class AttendanceForm(forms.ModelForm):

    class Meta:
        model=AttendanceRecord
        fields = ['emp_id','date','miti', 'day', 'in_time','out_time','punch_count','time_spent','difference_time']


class AllReport(forms.Form):
    a_nepali_date_from = forms.CharField()
    a_nepali_date_to = forms.CharField()


class SpecificEmpReport(forms.Form):
    emp_id = forms.IntegerField()
    nepali_date_from = forms.CharField(max_length=100)
    nepali_date_to = forms.CharField(max_length=100)
