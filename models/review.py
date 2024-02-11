#!/usr/bin/python3
"""
module inherited from BaseModel
"""
from models.base_model import BaseModel
class Review(BaseModel):
    """
    Review model
    """
    Place_id = ""
    User_id = ""
    text = ""
