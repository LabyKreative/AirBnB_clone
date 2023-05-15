#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel  # noqa
from models.engine.file_storage import FileStorage  # noqa
from models.user import User  # noqa
from models.state import State  # noqa
from models.place import Place  # noqa
from models.city import City  # noqa
from models.amenity import Amenity  # noqa
from models.review import Review  # noqa
