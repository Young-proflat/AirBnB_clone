#!/usr/bin/python3
"""
doc
"""
import json


class FileStorage():
    """
    doc
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns a dictionary of
        all obj. class.id as key
        and obj as
        """
        return FileStorage.__objects

    def save(self):
        """
        adds a new obj to the storage
        """
        Dictionary = {attr: value.to_dict() for attr, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(Dictionary, f)

    def new(self, obj):
        """
        add a new obj dictionary
        """
        class_name = obj.__class__.__name__
        FileStorage.__objects[class_name + "." + obj.id] = obj

    def reload(self):
        """
        reloads all the objs saved in file
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.amenity import Amenity
        from models.city import City
        from models.state import State
        from models.review import Review
        MyClasses = {"BaseModel": BaseModel, "User": User, "Place": Place,
                     "Amenity": Amenity, "City": City, "State": State,
                     "Review": Review}
        try:
            with open(FileStorage.__file_path, "r") as f:
                Dictionary = json.load(f)
                for attr, value in Dictionary.items():
                    FileStorage.__objects[attr] = MyClasses[value["__class__"]](**value)
        except Exception:
            pass

    def destroy(self, key):
        if key in FileStorage.__objects:
            del (FileStorage.__objects[key])
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects, f)
