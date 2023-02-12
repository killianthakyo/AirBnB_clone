#!/usr/bin/python3
"""
Class BaseModel that defines all common attriibutes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """
    Initialise BaseModel class with attributes
    """
    def __init__(self, *args, **kwargs):
        """
        Initialise attributes
        """
        if (len(kwargs) != 0):
            form = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                    continue
                if key == "created_at":
                    self.created_at = datetime.strptime(value, form)
                    continue
                if key == "updated_at":
                    self.updated_at = datetime.strptime(value, form)
                    continue
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def save(self):
        """
        Update the public instance attribute updated_at with current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """REturn dictionary containing all keys/values"""
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.__name__
        cp_dct['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        cp_dct['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return (cp_dct)

    def __str__(self):
        """
        Returns a human readable string
        """
        cname = self.__class__.__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)
