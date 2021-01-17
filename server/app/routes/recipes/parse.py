from flask_restful import reqparse, Resource
from recipe_scrapers import scrape_me, WebsiteNotImplementedError
from app.model import RecipeModel

parse_post = reqparse.RequestParser()
parse_post.add_argument(
    'source_url',
    required = True,
    nullable = False,
    help = 'A source url is required.'
)

class RecipesParse(Resource):
    def post(self):
        try:
            args = parse_post.parse_args(strict=True)
            source_url = args['source_url']
            scraper = scrape_me(source_url)
            result = RecipeModel(
                title = scraper.title(),
                source_url = source_url,
                author = scraper.author(),
                total_time = scraper.total_time(),
                yields = scraper.yields(),
                image_url = scraper.image(),
                ingredients = scraper.ingredients(),
                instructions = scraper.instructions().split('\n'),
                ratings = scraper.ratings()
            )
            return { 'data': result.encode() }, 200
        except WebsiteNotImplementedError as wnie:
            return { 'exception': str(wnie) }, 400
        return { 'exception': 'Unknown parsing error occured.' }, 500