#!/usr/bin/python3
"""DB Storage Module"""

from sqlalchemy.orm.session import Session
from models.base_model import Base, BaseModel
from os import getenv
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """DB Storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Class constructor"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if (getenv("HBNB_ENV") == "test"):
            Base.metadata.drop_all(self.__engine)
        new_session = sessionmaker(bind=self.__engine)
        self.__session = new_session()

    def all(self, cls=None):
        """Query in current db all objs deptending of cls name"""
        ret_dict = {}
        classes = []

        if cls is None:
            classes = [
                    BaseModel, User, Place,
                    State, City, Amenity, Review
                    ]
        else:
            classes = [cls]

        for i in range(0, len(classes)):
            for inst in self.__session.query(classes[i]):
                ret_dict[classes[i].__name__ + "." + inst.id] = inst

        return ret_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and the current db session"""
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()

    def close(self):
        '''Closes'''
        self.__session.close()
