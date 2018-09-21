from sqlalchemy import create_engine

from django.conf import settings


class DbConnect():
    def __init__(self):
        self.user = settings.DATABASES['default']['USER']
        self.password = settings.DATABASES['default']['PASSWORD']
        self.database_name = settings.DATABASES['default']['NAME']

    def db_connect(self):
        database_url = 'sqlite:///db.sqlite3'

        self.engine = create_engine(database_url, echo=False)
