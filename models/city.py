#!/usr/bin/python3
"""
This is City module
"""

from .base_model import BaseModel


class City(BaseModel):
	"""
	why is my intelesense working
	"""

	state_id = ""
	name = ""


	def __init__(self, *args, **kwargs):
		"""
		This initializes the class
		"""
		super().__init__(*args, **kwargs)