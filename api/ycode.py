
from flask import Flask, current_app, request
from flask.ext.restful import Resource, reqparse
from flask.ext.mongokit import MongoKit, Document
from bson.objectid import ObjectId

from shell import Shell
from dbschema import TestCaseDocumentModel

class TestCode(Resource):
    def post(self):
    	sh = Shell()

    	for line in request.form['code'].split('\n'):
    		retval = sh.push(line)

        return {'retval': retval.strip() }



# Fetches list view and in detail view of a Test Case.
class GetTestCase(Resource):

    def __init__(self):
        super(GetTestCase, self).__init__()


    def get(self, testcase_id=None):

        final = ''
        if testcase_id is None:
            newList = list (current_app.db.TestCaseDocumentModel.find())
            print newList
            final =  {'retval' : str(len(newList)) + ' Records Located' }
        else:
            print   'testcase_id = ', testcase_id

            try:
                valid_id = ObjectId(testcase_id)
            except:
                # return a flag
                final = { 'retval':  'in valid objectid' }
                return final, 400
            else:
                new_test_case = current_app.db.TestCaseDocumentModel.get_from_id (valid_id)
                print new_test_case
                final = {'retval' : 'located - exact' }

        return final
