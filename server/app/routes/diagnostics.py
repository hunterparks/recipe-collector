from flask_restful import Resource

class Info(Resource):
    def get(self):
        return {
            'version': '1.0.0'
        }
