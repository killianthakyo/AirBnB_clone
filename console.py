#!/usr/bin/python3
"""
Colsole that contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_EOF(self, line):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def do_quit(self, line):
        return True

    def help_quit(self):
        print('\n'.join(['Quit command to exit the program\n']))

if __name__ == '__main__':
    HBNBCommand().cmdloop()

