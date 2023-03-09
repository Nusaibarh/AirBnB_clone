#!/usr/bin/python3
"""
This module is for state
"""

from .base_model import BaseModel


class State(BaseModel):
	"""
	This is a state class
	"""

	name = ""

	def __init__(self, *args, **kwargs):
		"""
		initializes the class to do it
		"""
		super().__init__(*args, **kwargs)