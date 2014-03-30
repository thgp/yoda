
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





# Create New Test Case -
# Basic implementation - Future requirement link to Code Collection
class NewTestCase(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('code', type = str, required = True, help = 'No code submitted', location = 'form')
        self.reqparse.add_argument('description',  type = str, default = "", location = 'form')
        self.reqparse.add_argument('function_reference', type = str, required = True, help = 'No Reference Function Name', location = 'form')
        self.reqparse.add_argument('function_student', type = str, required = True, help = 'No Student Function Given', location = 'form')
        self.reqparse.add_argument('num_inputs',   type = int, required = True, help = 'Number of Function Inputs Not Given', location = 'form')
        super(NewTestCase, self).__init__()

    # ...
    def post(self):
        '''code: , if_name: num_inputs:   student_function:   array - testcases: input_1 ...      '''
        '''test case will look like [ { } ] '''
        # print current_app.db
        args = self.reqparse.parse_args()

        tcase = current_app.db.TestCaseDocumentModel()
        tcase.code = unicode(args['code'])
        tcase.function_reference = unicode(args['function_reference'])
        tcase.function_student = unicode(args['function_student'])
        tcase.num_inputs = args['num_inputs']
        tcase.save()
        return { 'message': 'success' }
