#!/usr/bin/python3
"""AirBnB Console"""

from models.base_model import BaseModel
import cmd
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """Myconsole Class"""

    prompt = "(hbnb) "
    
    class_name = ["BaseModel"]

    def do_create(self, line):
        """The create method"""
        input_command = shlex.split(line)

        if len(input_command) == 0:
            print("** class name missing **")
        elif input_command[0] not in self.class_name:
            print("** class doesn't exist **")
        else:
            class_inst = BaseModel()
            class_inst.save()
            print(class_inst.id)

    def do_show(self, line):
        """ Prints the string representation of the class name and id"""
        input_command = shlex.split(line)

        if len(input_command) == 0:
            print("** class name missing **")
        elif input_command[0] not in self.class_name:
            print("** class doesn't exist **")
        elif len(input_command) < 2:
            print("** instance id missing **")
        else:
            obj  = storage.all()

            key = "{}.{}".format(input_command[0], input_command[1])
            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")

    def do_update(sef, line):
        """Updates an instance based on the class name and id"""
        pass

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        input_command = shlex.split(line)

        if len(input_command) == 0:
            print("** class name missing **")
        elif input_command[0] not in self.class_name:
            print("** class doesn't exist **")
        elif len(input_command) < 2:
            print("** instance id missing **")
        else:
            obj  = storage.all()

            key = "{}.{}".format(input_command[0], input_command[1])
            if key in obj:
                del obj[key]
                storage.save()

            else:
            print("** no instance found **")


    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name"""
        obj  = storage.all() 
            

    def do_EOF(self, line):
        """Exits the console gracefully. Usage: Ctrl D"""
        print()
        return True

    def help_EOF(self):
        """EOF command. Usage: Ctrl D"""
        print("Exits the console gracefully. Usage: Ctrl D")

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Quit command. Usage: quit"""
        print("Quit command to exit the program")

    def emptyline(self):
        """This line prints nothing"""
        pass


if __name__ == "__main__":
    """Entry point for the AirBnB Console."""
    HBNBCommand().cmdloop()
