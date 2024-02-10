#!/usr/bin/python3
"""
BaseModel Module
"""
import uuid
from . import storage
from datetime import datetime
class BaseModel:
    """
    declaring the class
    """
    def __init__(self, *args, **kwargs):
        """
        instantiating new object
        """
        for attribute, value in kwargs.items():
            if attribute == "__class__":
                continue
            if attribute == "created_at" or attribute == "updated_at":
                self.attribute = (datetime.fromisoformat(value))
            else :
                self.attribute = value
        else:
            self.id = (uuid.uuid4())
            self.created_at = (datetime.now())
            self.updated_at = (datetime.now())
            storage.new(self)
            
    def __str__(self):
        """
        to return attribute in string format
        """
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
    
    def save(self):
        """
        updating the instant public 
        attribute with the current database
        """
        storage.safe()
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """
        This method returns key and value
        in dictionary format
        """
        Dictionary = {}
        for attribute, value in self.__dict__.items():
            if attribute == "updated_at" or attribute == "created_at":
                Dictionary[attribute] = value.isoformat()
            else:
                Dictionary[attribute] = value
                Dictionary[__class__] = self.__class__.__name__
                return Dictionary
