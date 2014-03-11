import sys
from code import InteractiveConsole

from filecacher import FileCacher

class Shell(InteractiveConsole):
    "Wrapper around Python that can filter input/output to the shell"
    def __init__(self):
        self.stdout = sys.stdout
        self.cache = FileCacher()
        InteractiveConsole.__init__(self)
        return

    def get_output(self): 
    	sys.stdout = self.cache
    	return sys.stdout
    
    def return_output(self): 
    	sys.stdout = self.stdout
    	return sys.stdout

    def push(self,line):
        self.get_output()
        # you can filter input here by doing something like
        # line = filter(line)
        InteractiveConsole.push(self,line)
        self.return_output()
        output = self.cache.flush()
        # you can filter the output here by doing something like
        # output = filter(output)
        return output # or do something else with it

