#!/usr/bin/python3
"""
This is the console necessary for the project
This is a commnent
I reaaly do not understand documentation again
"""

import cmd
import json
import os

from models.base_model import BaseModel
from models import storage
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """
    This is my console class
    """

    prompt = '(hbnb) '
    clsnms = {
                "BaseModel":BaseModel,
                "User":User,
                "City":City,
                "State":State,
                "Amenity":Amenity,
                "Place":Place,
                "Review":Review
            }

    def emptyline(self):
        """
        Do nothing when no command entered
        """
        pass

    def do_quit(self, s):
        """
        Quits the program
        """
        return True

    def help_quit(self):
        """
        documantation for quit
        """
        print("Quit command to exit the program")

    do_EOF = do_quit
    help_EOF = help_quit

    def do_create(self, arg):
        """
        Creates a new user
        """
        if arg in self.clsnms:
            newuser = self.clsnms[arg]()
            newuser.save()
            print(newuser.id)
        elif arg == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        show a class intance and print string representation
        """
        storage.reload()
        objdict = storage.all()
        if arg == "":
            print("** class name missing **")
        else:
            splitted = arg.split()
            if splitted[0] not in self.clsnms:
                print("** class doesn't exist **")
                return
            if len(splitted) == 1:
                print("** instance id missing **")
                return
            basekey = "{}.{}".format(splitted[0], splitted[1])
            if basekey not in objdict:
                print("** no instance found **")
                return
            olduser = self.clsnms[splitted[0]](**objdict[basekey])
            print(olduser)

    def do_destroy(self, arg):
        """
        Deletes an instance based on class name
        """
        storage.reload()
        objdict = storage.all()
        if arg == "":
            print("** class name missing **")
        else:
            splitted = arg.split()
            if splitted[0] not in self.clsnms:
                print("** class doesn't exist **")
                return
            if len(splitted) == 1:
                print("** instance id missing **")
                return
            basekey = "{}.{}".format(splitted[0], splitted[1])
            if basekey not in objdict:
                print("** no instance found **")
            else:
                del objdict[basekey]
            with open("file.json", "w") as file:
                json.dump(objdict, file)

    def do_all(self, arg):
        """
        prints a list of string representation of all instance
        if a class name is specified, all instance of the class is printed.
        """
        storage.reload()
        instances = storage.all()
        classes = []
        if arg == "":
            pass
        elif arg not in self.clsnms:
            print("** class doesn't exist **")
            return
        for key in instances.keys():
            ss = key.split(".")
            inst = self.clsnms[ss[0]](**instances[key])
            if arg == "":
                classes.append(str(inst))
            elif inst.__class__.__name__ == arg:
                classes.append(str(inst))
        print(classes)

    def do_update(self, arg):
        """
        From here we try to update certain atrributes,
        one at a time
        """
        storage.reload()
        objdict = storage.all()
        if arg == "":
            print("** class name missing **")
        else:
            splitted = arg.split()
            if splitted[0] not in self.clsnms:
                print("** class doesn't exist **")
                return
            if len(splitted) == 1:
                print("** instance id missing **")
                return
            basekey = "{}.{}".format(splitted[0], splitted[1])
            if basekey not in objdict:
                print("** no instance found **")
                return
            if len(splitted) == 2:
                print("** attribute name missing **")
                return
            if len(splitted) == 3:
                print("** value missing **")
                return
            clsdict = objdict.get(basekey)
            try:
                value = int(splitted[3])
            except Exception:
                value = str(splitted[3].strip('"\''))
            clsdict.update({splitted[2]: value})
            objdict.update({basekey: clsdict})
            with open("file.json", "w") as file:
                json.dump(objdict, file)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
