# AirBnB_clone
AirBnB Clone Project
An implementation of AirBnB like project.
The cmd module contains one public class, Cmd, designed to be used as a base class for command processors such as interactive shells and other command interpreters.

Example

import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    
    def do_greet(self, line):
        print "hello"
    
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()
