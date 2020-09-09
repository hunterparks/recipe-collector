from flask_restful import Resource
import os

class Info(Resource):
    def get(self):
        return {
            'version': os.getenv('APP_VERSION')
        }
