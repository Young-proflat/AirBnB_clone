#!/usr/bin/python3
"""
Marking the models directory 
as a package
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
