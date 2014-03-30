from flask import Flask
from flask.ext.restful import Api
from flask.ext.mongokit import MongoKit, Document

# import database schema(s)
from dbschema import TestCaseDocumentModel

import ycode


def create_app():
    app = Flask(__name__)
    api = Api(app)

    # add api endpoint basic code evaluation
    api.add_resource(ycode.TestCode, '/')

    # add api endpoint testcase list view and detail view of testcase based on Object ID
    api.add_resource(ycode.GetTestCase, '/testcases', '/testcases/<string:testcase_id>')

    # TODO:  Check if MongoDB is up and running (this requires a unit testing framework)
    app.db = MongoKit (app)

    # Register MongoDB - TestCaseDocumentModel
    app.db.register([TestCaseDocumentModel])


    @app.errorhandler(500)
    def internal_error(exception):
        return "Some internal error has taken place.  Alert somebody!"

    return app

# Make sure you are calling create_app func below:
app = create_app()
