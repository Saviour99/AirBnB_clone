#!/usr/bin/python3
"""AirBnB Console"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Myconsole Class"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exits the console gracefully. Usage: Ctrl D"""
        print()
        return True

    def help_EOF(self):
        """EOF command. Usage: Ctrl D"""
        print("Exits the console gracefully. Usage: Ctrl D")

    def do_quit(self, line):
        """Exits the console gracefully. Usage: quit"""
        return True

    def help_quit(self):
        """Quit command. Usage: quit"""
        print("Exits the console gracefully. Usage: quit")

    def emptyline(self):
        """This line prints nothing"""
        pass


if __name__ == "__main__":
    """Entry point for the AirBnB Console."""
    HBNBCommand().cmdloop()
