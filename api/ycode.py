from flask import Flask, request
from flask.ext.restful import Resource

from shell import Shell

class TestCode(Resource):
    def post(self):
    	sh = Shell()

    	for line in request.form['code'].split('\n'):
    		retval = sh.push(line)
    	
        return {'retval': retval.strip() }

