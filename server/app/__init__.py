import os
from flask import Flask
from flask_restful import Resource, Api

# Load environment variables
from dotenv import load_dotenv
from pathlib import Path
env_path = Path('..') / '.flaskenv'
load_dotenv(dotenv_path = env_path)

# Create Flask app and API
app = Flask(__name__)
api = Api(
    app = app,
    prefix = '/api/v1'
)

# Connect to database
from flask_pymongo import PyMongo

MONGO_USERNAME = os.getenv('MONGO_RC_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_RC_PASSWORD')
MONGO_HOST = os.getenv('MONGO_RC_HOST')
MONGO_PORT = os.getenv('MONGO_RC_PORT')
MONGO_DBNAME = os.getenv('MONGO_RC_DBNAME')

app.config['MONGO_URI'] = f'mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DBNAME}'
mongo = PyMongo(app)

# === MAIN ===

# Default Routes
from app.routes import Default
api.add_resource(Default, '/')

# Recipes Routes
from app.routes.recipes import RecipesCollection, Recipes
api.add_resource(RecipesCollection, '/recipes')
api.add_resource(Recipes, '/recipes/<string:id>')
from app.routes.recipes.parse import RecipesParse
api.add_resource(RecipesParse, '/recipes/parse')

# Diagnostics Routes
from app.routes.diagnostics import Info#, Status
api.add_resource(Info, '/info')
# api.add_resource(Status, '/status')

# 400 Bad Request – This means that client-side input fails validation.
# 401 Unauthorized – This means the user isn’t not authorized to access a resource. It usually returns when the user isn’t authenticated.
# 403 Forbidden – This means the user is authenticated, but it’s not allowed to access a resource.
# 404 Not Found – This indicates that a resource is not found.
# 500 Internal server error – This is a generic server error. It probably shouldn’t be thrown explicitly.
# 502 Bad Gateway – This indicates an invalid response from an upstream server.
# 503 Service Unavailable – This indicates that something unexpected happened on server side (It can be anything like server overload, some parts of the system failed, etc.).