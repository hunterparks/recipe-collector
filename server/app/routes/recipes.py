from flask_restful import Resource, abort

recipes = []

# Handles the collection
class RecipesResource(Resource):
    def get(self):
        return {
            'data': recipes
        }
    def post(self):
        return

# Handles the items in collection
class Recipes(Resource):
    def get(self, id):
        if id < len(recipes):
            return {
                'data': recipes[id]
            }
        else:
            abort(404, message = 'You\'re dumb.')