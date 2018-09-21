from datetime import datetime

from attendance.models import AttendanceRecord
import numpy as np
import pandas as pd
import cufflinks as cf

import plotly.plotly as plt
import plotly.graph_objs as go
import plotly.tools as tls


class Report:

    def get_all_employee_data(from_date, to_date):
        all_employee_list = AttendanceRecord.objects.filter(miti__gt=from_date, miti__lt=to_date).order_by(
            '-miti')

        return all_employee_list

    def get_specific_emp_data(from_date, to_date, e_id):
        specific_employee_list = AttendanceRecord.objects.filter(miti__gt=from_date, miti__lt=to_date,
                                                                 emp_id=e_id).order_by('-miti')

        return specific_employee_list


class Analytics:
    def get_emp_graph(e_id):
        tls.set_credentials_file(username='ashwinpradhan', api_key='OSTejAaNxLezI4RstNws')

        df = pd.DataFrame(list(AttendanceRecord.objects.filter(emp_id=e_id, ).values().order_by('date')))

        df['in_time'] = df['in_time'].apply(lambda x: format(datetime.strptime(x, '%H:%M:%S'), '%H:%M:%S'))
        df['out_time'] = df['out_time'].apply(lambda x: format(datetime.strptime(x, '%H:%M:%S'), '%H:%M:%S'))

        df['date'] = df['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d').date())
        df['miti'] = df['miti'].apply(lambda x: datetime.strptime(x, '%Y/%m/%d').date())

        print(df['in_time'])
        print(df['date'])

        trace1 = go.Scatter(
            x=df['date'],
            y=df['in_time'],
            name='In Time',
            mode='markers+lines',
            text=e_id,
            line=dict(color='#17BECF'),
        )

        trace2 = go.Scatter(
            x=df['date'],
            y=df['out_time'],
            name='Out Time',
            mode='markers+lines',
            text=e_id,
            line=dict(color='#7F7F7F'),
        )

        data = [trace1, trace2]
        layout = go.Layout(title="Time Analysis", showlegend=True,yaxis=dict(autorange=True))
        fig = go.Figure(data=data, layout=layout)
        div = plt.plot(fig, filename='d3', auto_open=False)
        print(div)
        return div
