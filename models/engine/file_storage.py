#!/usr/bin/python3
"""
Class to serialize instances to JSON and deserialise JSON to instances
"""
import json
from models.base_model import BaseModel
import models


class FileStorage():
    """Instanciate FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """REturns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in object with key and values"""
        key = str(obj.__class__.__name__) + '.' + str(obj.id)
        val = obj
        FileStorage.__objects[key] = val

    def save(self):
        """
            Serializes __objects attribute to JSON file.
        """
        with open(FileStorage.__file_path, "w") as f:
            my_dict = {key: val.to_dict() for key, val in
                       FileStorage.__objects.items()}
            json.dump(my_dict, f)

    def reload(self):
        """Deserialises json string to objecct"""
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as f:
                FileStorage.__objects = json.load(f)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass
