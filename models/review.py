#!/usr/bin/python3
"""
This is a review module
"""

from .base_model import BaseModel


class Review(BaseModel):
	"""
	This is the review class
	"""

	place_id = ""
	user_id = ""
	text = ""

	def __init__(self, *args, **kwargs):
		"""
		This is INitializes the class
		"""
		super().__init__(*args, **kwargs)
