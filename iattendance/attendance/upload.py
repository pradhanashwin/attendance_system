import pandas as pd
from .dbconnect import DbConnect


class Upload(DbConnect):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def data_preprocess(self):
        self.data = self.data[
            ['EMPLOYEE ID', 'DATE', 'MITI','DAY', 'IN TIME', 'OUT TIME', 'PUNCH COUNT','DIFF (MINUTE)', 'ACTUAL (MINUTE)']]
        self.data.columns = ['emp_id_id', 'date', 'miti','day', 'in_time', 'out_time', 'punch_count', 'time_spent',
                             'difference_time']

    def csv_upload(self):
        self.data.to_sql(name='AttendanceRecord', con=self.engine, if_exists='append', index=False )

    def upload_csv_database(self):
        self.data_preprocess()
        self.db_connect()
        self.csv_upload()
        self.engine.dispose()


    def emp_preprocess(self):
        self.data = self.data[
            ['ID No.', 'Name']]
        self.data.columns = ['emp_id', 'name']

    def emp_upload(self):
        self.data.to_sql(name='Employee', con=self.engine, if_exists='append', index=False )

    def upload_emp_database(self):
        self.emp_preprocess()
        self.db_connect()
        self.emp_upload()
        self.engine.dispose()

