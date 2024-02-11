#!/usr/bin/python3
"""
storage module
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
        Dictionary = {}
        for attr, value in FileStorage._objects.items():
            Dictionary[attr] = value.to_dict()
        with open(FileStorage._file_path, "w") as f:
            json.dump(Dictionary, f)
            
    def reload(self):
        """
        deserializes the JSON file
        """
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        
        MyClasses = {"BaseModel": BaseModel, "User": User, "Place": Place,
                    "Amenity": Amenity, "City": City, "State": State,
                    "Review": Review}
        try:
            with open(FileStorage._file_path, "r") as f:
                Dictionary = json.load(f)
            for attr, value in Dictionary.items():
                FileStorage._objects[attr] = MyClasses[value["__class__"]](**value)
        except Exception:
            pass
        
    def destroy(self, key):
        """
        Doc
        """
        if key in FileStorage.__objects:
            del (FileStorage.__objects[key])
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects, f)
