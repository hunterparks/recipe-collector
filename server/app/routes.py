from flask_restful import Resource
from app import app

class HelloWorld(Resource):
        def get(self):
                return { 'hello': 'world' }

# @app.route('/')
# @app.route('/index')
# def index():
#         return "Hello, World!"
