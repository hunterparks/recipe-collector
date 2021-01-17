from flask_restful import reqparse, Resource
from app import mongo
from app.model import RecipeModel
from datetime import datetime
from bson.objectid import ObjectId

recipes_collection_post = reqparse.RequestParser()
recipes_collection_post.add_argument(
    'title',
    required = True,
    nullable = False,
    help = 'A recipe title is required.'
)
recipes_collection_post.add_argument(
    'author',
    required = True,
    nullable = False,
    help = 'A recipe author is required.'
)
recipes_collection_post.add_argument(
    'source_url',
    required = True,
    nullable = False,
    help = 'A recipe source url is required.'
)
recipes_collection_post.add_argument(
    'image_url',
    required = True,
    nullable = False,
    help = 'A recipe image url is required.'
)
recipes_collection_post.add_argument(
    'total_time',
    required = True,
    nullable = False,
    help = 'A recipe total time is required.'
)
recipes_collection_post.add_argument(
    'yields',
    required = True,
    nullable = False,
    help = 'A recipe yields is required.'
)
recipes_collection_post.add_argument(
    'ingredients',
    required = True,
    nullable = False,
    help = 'A recipe ingredients is required.'
)
recipes_collection_post.add_argument(
    'instructions',
    required = True,
    nullable = False,
    help = 'A recipe instructions is required.'
)
recipes_collection_post.add_argument(
    'ratings',
    required = True,
    nullable = False,
    help = 'A recipe ratings is required.'
)

# Handles Collection of Recipes
class RecipesCollection(Resource):
    def get(self):
        recipes_cursor = mongo.db.recipe.find({ 'deleted_at': None })
        recipes = []
        for recipe in recipes_cursor:
            recipes.append(RecipeModel.decode(recipe).encode())
        return { 'data': recipes }, 200
    def post(self):
        args = recipes_collection_post.parse_args(strict = True)
        now = datetime.utcnow()
        args['created_at'] = now
        args['updated_at'] = now
        result = mongo.db.recipe.insert_one(args)
        if result.acknowledged:
            return { 'message': f'Recipe {result.inserted_id} was created.' }, 201
        else:
            return { 'exception': 'Unable to create recipe.' }, 500

# Handles Specific Recipes
class Recipes(Resource):
    def get(self, id):
        recipe = mongo.db.recipe.find_one({ '_id': ObjectId(id), 'deleted_at': None })
        if recipe is not None:
            return { 'data': RecipeModel.decode(recipe).encode() }, 200
        else:
            return { 'exception': f'Unable to find recipe {id}' }, 404
    def delete(self, id):
        result = mongo.db.recipe.update_one({ '_id': ObjectId(id) }, { '$set': { 'deleted_at': datetime.utcnow() }})
        if result.modified_count == 1:
            return { 'message': f'Recipe {id} was deleted.' }, 200
        else:
            return { 'exception': 'Unable to delete recipe.' }, 404