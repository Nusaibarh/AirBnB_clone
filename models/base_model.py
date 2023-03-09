#!/usr/bin/python3
"""
This is the base model
it generates a unique id with uuid.uuid4()
created at date time 
can also update from json
this is all for now
"""

import uuid
from datetime import datetime
from . import storage

class BaseModel(object):
    """
    This is the base model
    """

    id = 0
    created_at = 0
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """
        This initializes the class with Id, Date and Time
        """
        if 'id' in kwargs:
                self.id = kwargs['id']
        else:
            self.id = str(uuid.uuid4())
        if 'created_at' in kwargs:
            self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.created_at = datetime.now()
        if 'updated_at' in kwargs:
            self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'my_number' in kwargs:
            self.my_number = kwargs['my_number']
        if 'id' not in kwargs:
            storage.new(self)
        for key in kwargs:
            if key not in dir(self):
                setattr(self, key, kwargs[key])

    def __str__(self):
        """
        This is a string representation of my class
        It returns the class name id and dictionary
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        This is a save method to save shits
        It also updates the save time to update at
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        This returns a dictionary serialized for json
        """
        serial = {}
        serial.update(self.__dict__)
        serial.update({'updated_at':self.updated_at.isoformat(), 'created_at':self.created_at.isoformat()})
        serial.update({'__class__':self.__class__.__name__})
        return serial
