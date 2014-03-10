from flask import Flask, request
from flask.ext.restful import Resource, Api

from code import InteractiveConsole

import sys


app = Flask(__name__)
api = Api(app)

class FileCacher:
    "Cache the stdout text so we can analyze it before returning it"
    def __init__(self): self.reset()
    def reset(self): self.out = []
    def write(self,line): self.out.append(line)
    def flush(self):
        output = '\n'.join(self.out)
        self.reset()
        return output

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


class TestCode(Resource):
    def post(self):
    	sh = Shell()

    	for line in request.form['code'].split('\n'):
    		retval = sh.push(line)
    	
        return {'retval': retval.strip() }

api.add_resource(TestCode, '/')

if __name__ == '__main__':
    app.run(debug=True)
