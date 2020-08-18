import os
from flask import Flask
from flask_restful import Resource, Api
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
env_path = Path('..') / '.flaskenv'
load_dotenv(dotenv_path = env_path)

# Create Flask app and API
app = Flask(__name__)
api = Api(
    app = app,
    prefix = '/api/v1'
)

# Default Routes
from app.routes import Default
api.add_resource(Default, '/')

# Recipes Routes
from app.routes.recipes import RecipesResource, Recipes
api.add_resource(RecipesResource, '/recipes')
api.add_resource(Recipes, '/recipes/<int:id>')

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