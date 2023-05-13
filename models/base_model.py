#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the base model of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel.

        Args:
            *args: Unused positional arguments.
            **kwargs: Key/value pairs of attributes.
        """
        timestamp_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, timestamp_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Updates the 'updated_at' attribute with the current datetime and save the model."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance.

        Includes the key/value pair '__class__' representing
        the class name of the object.
        """
        result = self.__dict__.copy()
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        result["__class__"] = self.__class__.__name__
        return result

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
