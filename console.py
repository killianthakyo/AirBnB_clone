#!/usr/bin/python3
"""
Colsole that contains the entry point of the command interpreter
"""
import cmd
import models
from models import storage
from models.base_model import BaseModel


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

    def do_create(self, args):
        """
         Create an instance of BaseModel if class exists
        """
        if args == "" or args is None:
            print('** class name missing **')
        elif args in models.classes:
            my_model = models.classes[args]()
            my_model.save()
            print(my_model.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Create an instance of BaseModel if class exists
        """
        argl = args.split(' ')
        objdict = storage.all()
        if args == '' or args is None:
            print('** class name missing **')
        elif len(argl) > 0 and argl[0] in models.classes:
            if len(argl) > 1:
                if "{}.{}".format(argl[0], argl[1]) not in objdict:
                    print("** no instance found **")
                else:
                    print(objdict["{}.{}".format(argl[0], argl[1])])
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """
        Create an instance of BaseModel if class exists
        """
        argl = args.split(' ')
        objdict = storage.all()
        if args == '' or args is None:
            print('** class name missing **')
        elif len(argl) > 0 and argl[0] in models.classes:
            if len(argl) > 1:
                if "{}.{}".format(argl[0], argl[1]) not in objdict:
                    print("** no instance found **")
                else:
                    del objdict["{}.{}".format(argl[0], argl[1])]
                    storage.save()
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """
         Create an instance of BaseModel if class exists
        """
        argl = args.split(' ')
        objdict = storage.all()
        if args == "" or args is None:
            obj_list = [str(obj) for key, obj in objdict.items()]
            print(obj_list)
        elif args in models.classes:
            obj_list = [
                    str(obj) for key, obj in objdict.items()
                    if type(obj).__name__ == argl[0]]
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """ Updates an instance based on the class name and id
        by adding or updating attribute """
        words = args.split(' ')
        if len(args) == 0:
            print("** class name missing **")
            return
        elif words[0] not in models.classes:
            print("** class doesn't exist **")
            return
        elif len(words) == 1:
            print("** instance id missing **")
            return
        if len(words) == 3:
            print("** value missing **")
            return
        s1 = words[0] + '.' + words[1]
        all_objs = storage.all()
        for key, value in all_objs.items():
            if s1 in key:
                if len(words) == 2:
                    print("** attribute name missing **")
                    return
                if words[3][0] == "\"" and words[3][-1] == "\"":
                    setattr(value, words[2], words[3][1:-1])
                    storage.save()
                    return
                setattr(value, words[2], words[3])
                storage.save()
                return
        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
