from datetime import datetime
from flask.ext.mongokit import MongoKit, Document

class TestCase(Document):
    __collection__ = 'testcases'
    structure = {
    	'testcase_id': int,
        'code': unicode,
        'description': unicode,
        'function_reference': unicode,
        'function_student': unicode,
        'num_inputs': int,
        'creation': datetime,
    }
    required_fields = ['code', 'function_reference', 'function_student', 'num_inputs']
    default_values = {'creation': datetime.utcnow()}
    use_dot_notation = True

