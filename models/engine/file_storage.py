#!/usr/bin/python3
"""File Storage Module"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """File storage class"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initialization of FileStorag object"""

        pass

    def all(self):
        """Return the dictionary"""

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj"""

        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""

        Total_obj = FileStorage.__objects
        serialization = {key: obj.to_dict() for key, obj in Total_obj.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialization, file)

    def reload(self):
        """deserializes the JSON file to __objects"""

        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "r") as file:
                    obj_dic = json.load(file)

                    for key, value in obj_dic.items():
                        class_name, obj_id = key.split(".")
                        eval_class_name = eval(class_name)
                        instance = eval_class_name(**value)
                        self.__objects[key] = instance

            except FileNotFoundError:
                pass

        else:
            pass
