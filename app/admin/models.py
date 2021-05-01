# coding: utf-8
from datetime import datetime

from sqlalchemy import Column, SmallInteger, String
from sqlalchemy.orm.collections import InstrumentedList

from app.common.db_util import db

Base = db.Model


class DBUtils:
    def json(self, *args):
        new_json = {}
        for col in self.__table__.columns:
            val = self.__getattribute__(col.name)
            new_json[col.name] = str(val) if not isinstance(val, int) and val is not None else val

        for rel in self.__mapper__.relationships:
            if rel.key in args:
                actual_model = self.__getattribute__(rel.key)
                if actual_model is not None:
                    if type(actual_model) is InstrumentedList:
                        for sub_model in actual_model:
                            if rel.key not in new_json:
                                new_json[rel.key] = []
                            new_json[rel.key].append(sub_model.json(*args))
                    else:
                        new_json[rel.key] = actual_model.json(*args)
                else:
                    new_json[rel.key] = None
        return new_json


class User(Base, DBUtils):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = Column(String(50), nullable=False)
    name = Column(String(50))
    phone = Column(String(20))
    company = Column(String(100))
    manager = Column(String(100))
    budget = Column(String(100))
    message = Column(String(3000))
    from_pg = Column(String(200))
    option_n = Column(db.Integer)
    status = Column(SmallInteger, nullable=False)
    created_since = db.Column(db.DateTime, default=datetime.now(), nullable=False)
