#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel  # noqa
from models.user import User  # noqa
from models.state import State  # noqa
from models.city import City  # noqa
from models.place import Place  # noqa
from models.amenity import Amenity  # noqa
from models.review import Review  # noqa


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The path to the file where objects are stored.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retrieve all objects.

        Returns:
            dict: A dictionary of all objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the storage.

        Args:
            obj (BaseModel): The object to be added.
        """
        obj_key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_key, obj.id)] = obj

    def save(self):
        """Save the objects to the file in JSON format."""

        obj_dict = FileStorage.__objects
        obj_dic = {obj: obj_dict[obj].to_dict() for obj in obj_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dic, f)

    def reload(self):
        """Reload objects from the file, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dic = json.load(f)
                for obj_data in obj_dic.values():
                    class_name = obj_data["__class__"]
                    del obj_data["__class__"]
                    self.new(eval(class_name)(**obj_data))
        except FileNotFoundError:
            return
