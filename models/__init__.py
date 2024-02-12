#!/usr/bin/python3
"""
Marking the models directory 
as a package
"""
from models.engine.FileStorage import FileStorage

storage = FileStorage()
storage.reload()
