#!/usr/bin/python3
"""
This is a module that stores are created classes
to json to string and back
"""

import json


class FileStorage:
    """
    This class does as described above
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns a dictionary in the object
        """
        return (self.__objects)

    def new(self, obj):
        """
        This method creates the dictionary of object saved
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects.update({key: obj.to_dict()})

    def save(self):
        """
        Now we need to serialize our object into json file
        """
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """
        We saved a file and need to convert it back to object
        file.json is loaded as dictionary into object attribute
        """
        try:
            with open(self.__file_path, "r") as fileread:
                self.__objects.update(json.load(fileread))
        except Exception:
            pass
