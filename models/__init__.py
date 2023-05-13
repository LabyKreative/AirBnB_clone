#!/usr/bin/python3
"""Initialize the models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
