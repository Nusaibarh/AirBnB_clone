#!/usr/bin/python3#
"""
This is the first User
It is a user Module
This is a comment
"""


from .base_model import BaseModel


class User(BaseModel):
	"""
	this is a User Class
	Nothing much just a few attributes
	This is a comment
	"""

	
	email = ""
	password = ""
	first_name = ""
	last_name = ""

	def __init__(self, *arg, **kwargs):
		"""
		Initializer attribute
		This is a comment
		"""
		super().__init__(*arg, **kwargs)