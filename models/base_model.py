#!/usr/bin/python3
"""
Class BaseModel that defines all common attriibutes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """
    Initialise BaseModel class with attributes
    """
    def __init__(self, *args, **kwargs):
        """
        Initialise attributes
        """
        if (len(kwargs) != 0):
            frm = "%Y-%m-%dT%H:%M:%S.%f"
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"], frm)
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], frm)
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

    def save(self):
        """
        Update the public instance attribute updated_at with current datetime
        """
        self.updated_at = datetime.today()

    def to_dict(self):
        """REturn dictionary containing all keys/values"""
        dct = self.__dict__.copy()
        dct["__class__"] = self.__class__.__name__
        dct["created_at"] = self.created_at.isoformat()
        dct["updated_at"] = self.updated_at.isoformat()
        return dct

    def __str__(self):
        """
        Returns a human readable string
        """
        cname = self.__class__.__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)
