#!/usr/bin/python3
"""
Creating an instance of FileStorage and calling
 an instance of it
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

classes = {"BaseModel": BaseModel, "User": User}

storage = FileStorage()
storage.reload()
