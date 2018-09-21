from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from .report import Report, Analytics
import pandas as pd

from attendance.upload import Upload
from .forms import UploadEmpInfo, AllReport, SpecificEmpReport
from .models import Employee

import numpy as np
import plotly.graph_objs as go
import plotly.offline as ply

from rest_framework.views import APIView
from rest_framework.response import Response




@login_required
def load_home(request):
    return render(request, 'attendance/home.html')


@login_required
def load_upload_attendance(request):
    return render(request, 'attendance/upload_attendance.html')


@login_required
def upload_csv(request):
    if request.method == 'POST':
        csv_file = pd.read_excel(request.FILES['file'])
        upload_db = Upload(csv_file)
        upload_db.upload_csv_database()
        messages.success(request, 'The file was successfully uploaded!')
        return render(request, 'attendance/upload_attendance.html')

    else:
        messages.error(request, 'The file was not uploaded. Make sure you are uploading csv file!')
        return render(request, 'attendance/upload_attendance.html')


@login_required
def upload_emp_info(request):
    if request.method == 'POST':
        csv_file = pd.read_excel(request.FILES['file'])

        upload_db = Upload(csv_file)
        upload_db.upload_emp_database()
        messages.success(request, 'Employee Info was successfully uploaded!')
        return render(request, 'attendance/upload_employee_info.html')

    else:
        messages.error(request, 'The file was not uploaded. Make sure you are uploading csv file!')
        return render(request, 'attendance/upload_employee_info.html')

    # if request.method == 'POST':
    #     form = UploadEmpInfo(request.POST)
    #
    #     if form.is_valid():
    #         emp = Employee()  # Employee Model Instantiated
    #
    #         emp.emp_id = form.cleaned_data['emp_id']
    #         emp.name = form.cleaned_data['name']
    #         emp.department_id = form.cleaned_data['department_id']
    #         emp.position = form.cleaned_data['position']
    #         emp.save()
    #
    #         messages.success(request, 'Employee Info was successfully uploaded!')
    #         return render(request, 'attendance/upload_employee_info.html')
    #
    #     else:
    #         messages.error(request, 'Employee Info was not uploaded. Something is Wrong!')
    #         return render(request, 'attendance/upload_employee_info.html')
    # else:
    #     return render(request, 'attendance/upload_employee_info.html')


@login_required
# @user_passes_test(is_hr)
def load_all_employee_form(request):
    return render(request, 'attendance/all_report_template.html')


@login_required
# @user_passes_test(is_hr)
def all_employee_report(request):
    if request.method == 'GET':

        form = AllReport(request.GET)

        if form.is_valid():
            nepali_date_from = form.cleaned_data['a_nepali_date_from']
            nepali_date_to = form.cleaned_data['a_nepali_date_to']

            # changing the format of date to match the format with database
            nepali_date_from = "/".join((nepali_date_from).split("-"))
            nepali_date_to = "/".join((nepali_date_to).split("-"))
            print(nepali_date_from)
            args = Report.get_all_employee_data(nepali_date_from, nepali_date_to)
            all_datas = []
            for data in args:
                time_spent = min_to_hm(data.time_spent)
                full_data = {
                    'time_spent': time_spent,
                    'args': data,
                }
                print(time_spent)
                all_datas.append(full_data)

            # print(args)

            return render(request, 'attendance/all_employee_report.html', {'table': all_datas})

        else:

            return render(request, 'attendance/all_report_template.html')


@login_required
# @user_passes_test(is_hr)
def specific_employee_report(request):
    if request.method == 'GET':

        form = SpecificEmpReport(request.GET)

        if form.is_valid():
            emp_id = form.cleaned_data['emp_id']
            nepali_date_from = form.cleaned_data['nepali_date_from']
            nepali_date_to = form.cleaned_data['nepali_date_to']

            # changing the format of date to match the format with database
            nepali_date_from = "/".join((nepali_date_from).split('-'))
            nepali_date_to = "/".join((nepali_date_to).split('-'))

            args = Report.get_specific_emp_data(nepali_date_from, nepali_date_to, emp_id)
            sum_time = 0
            count = 0
            for emp in args:
                sum_time = sum_time + emp.time_spent
                count = count + 1
                avg_time = sum_time / count
            avg_time_spent = min_to_hm(avg_time)

            all_datas = []
            for data in args:
                time_spent = min_to_hm(data.time_spent)
                full_data = {
                    'time_spent': time_spent,
                    'args': data,
                }
                print(time_spent)
                all_datas.append(full_data)


            return render(request, 'attendance/specific_employee_report.html', {'table': all_datas,
                                                                                'avg_time_spent': avg_time_spent})

    return render(request, 'attendance/specific_report_template.html')






@login_required
# @user_passes_test(is_hr)
def specific_employee_analytics(request,emp_id_id):
    print(emp_id_id)
    plot = Analytics.get_emp_graph(emp_id_id)
    plot_url=str(plot)
    return render(request, 'attendance/specific_employee_analytics.html', {'graph': plot_url})





def min_to_hm(mytime):
    hour = int(mytime // 60)
    if len(str(hour)) == 1:
        hour = "0" + str(hour)

    minute = int(mytime % 60)
    if len(str(minute)) == 1:
        minute = "0" + str(minute)

    hm = (hour, minute)
    return hm


