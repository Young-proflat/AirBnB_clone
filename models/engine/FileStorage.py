#!/usr/bin/python3
"""
File storage module
"""

import json

class FileStorage:
     """
    serializing instance to json file
    and deserialize json file to instance
    """
    def __init__(self):
        self._file_path = "file.json"
        self._objects = {}
        
    def all(self):
        """
        returns the dictionary
        """
        return FileStorage._objects
    
    def new(self, obj):
        """
        This is to add new object
        """
        ClassName = obj.__class__.__name__
        FileStorage._objects[ClassName + "." + obj.id] = obj
        
    def save(self):
        """
        add the object to the storage
        """
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage._objects, f)
            
    def reload(self):
        """
        deserializes the JSON file
        """
        try:
            with open(FileStorage._file_path, "r") as f:
                my_dict = json.load(f)
        except Exception:
            pass
