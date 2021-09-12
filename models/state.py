#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base
from models.city import City
from models import storage
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            '''Cities relation with state'''
            ret = []
            cities_objs = storage.all(City)
            for key in cities_objs:
                if cities_objs[key].state_id == self.id:
                    ret.append(cities_objs[key])
            return ret
