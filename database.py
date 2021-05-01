import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.config import app_config


class DBConnection:
    session = None
    engine = None

    def __init__(self):
        self.engine = create_engine(app_config[os.getenv('FLASK_ENV')].SQLALCHEMY_DATABASE_URI, echo=True)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_session(self):
        return self.session

    def close(self):
        self.session.close()
        self.engine.dispose()
