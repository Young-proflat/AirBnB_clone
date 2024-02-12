#!/usr/bin/python3
"""
base_model module
"""
import uuid
from datetime import datetime
from . import storage


class BaseModel():
    """
    class BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        instantiating new obj
        """
        if kwargs:
            for attr, value in kwargs.items():
                if attr == "__class__":
                    continue
                if attr == "created_at" or attr == "updated_at":
                    setattr(self, attr, (datetime.fromisoformat(value)))
                else:
                    setattr(self, attr, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = (datetime.now())
            storage.new(self)

    def __str__(self):
        """
        string representation of obj
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        update the updated_at attribute
        to the last time the obj was saved
        """
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        edited default dictionary
        representation of object
        Returns: dict. attribute as
        key and attribute values as value
        """
        Dictionary = {}
        for attr, value in self.__dict__.items():
            if attr == "updated_at" or attr == "created_at":
                Dictionary[attr] = value.isoformat()
            else:
                Dictionary[attr] = value
        Dictionary["__class__"] = self.__class__.__name__
        return Dictionary
