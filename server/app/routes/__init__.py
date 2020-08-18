from flask_restful import Resource

class Default(Resource):
    def get(self):
        return { 'data': 'Hello there! Let\'s make some great food!' }