#!/usr/bin/python3
"""Base Model"""


import uuid
from datetime import datetime
import models
class BaseModel:
    """
    BaseModel class that defines all common attributes/method for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initialiazation of the BaseModel Object"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                elif key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Update the current datetime"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Change an instance to dictionary"""

        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict

    def __str__(self):
        """Return the string representation of the object"""

        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
