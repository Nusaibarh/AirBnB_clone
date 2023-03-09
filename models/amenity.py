#!/usr/bin/python3
"""
This is a comment
This commeent is for amenity
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
	"""
	The Amenity class inheriting from BaseModel
	Etra attribute name
	"""

	name = ""

	def __init__(self, *args, **kwargs):
		"""
		This initislizes the class
		"""
		super().__init__(*args, **kwargs)