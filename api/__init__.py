from flask import Flask
from flask.ext.restful import Api

import ycode

app = Flask(__name__)
api = Api(app)

api.add_resource(ycode.TestCode, '/')

if __name__ == '__main__':
    app.run(debug=True)
