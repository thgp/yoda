from flask import Flask, request
from flask.ext.restful import Resource

from shell import Shell


# List with Dictionary for a test module
TEST_LIST = [{'function_name': 'runMe', 'num_inputs': 1, 'input_1': 5, 'output_type': 'int', 'output': 25}, 
             {'function_name': 'runMe', 'num_inputs': 1, 'input_1': 2, 'output_type': 'int', 'output': 10}]


             
class TestCode(Resource):
    def post(self):

    	sh = Shell()
        
        for line in request.form['code'].split('\n'):
            retval = sh.push(line)


        if request.form['test_id']:
            final_result = {}
            test_id = request.form['test_id']
            
            # query db for all test_case with this test_id
            test_list = TEST_LIST
            count = 0; 
            for testCase in test_list:
                count = count + 1

                #create test string
                # to do build a function to test create and encode test string
                testString = unicode(testCase['function_name'] +'('+ str(testCase['input_1']) +')')
                # print testString

                retval = sh.push(testString)

                
                tc = 'test_case_'+ str(count)
                # newval = retval.strip()
                # chkval = testCase['output']

                # print type(newval), type(chkval)


                if retval.strip() == str(testCase['output']):
                    final_result[tc] = 'pass' + ' result  = ' + retval.strip()
                else:
                    final_result[tc] = 'fail' + ' result  = ' + retval.strip()
                
            return final_result 

        return { 'retval' : retval.strip() }
