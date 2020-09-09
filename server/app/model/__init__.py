import json

class RecipeModel:
    def __init__(
        self,
        _id = None,
        title = None,
        source_url = None,
        author = None,
        total_time = None,
        yields = None,
        image_url = None,
        ingredients = None,
        instructions = None,
        ratings = None,
        created_at = None,
        updated_at = None
    ):
        self._id = _id
        self.title = title
        self.source_url = source_url
        self.author = author
        self.total_time = total_time
        self.yields = yields
        self.image_url = image_url
        self.ingredients = ingredients
        self.instructions = instructions
        self.ratings = ratings
        self.created_at = created_at
        self.updated_at = updated_at
    def encode(self):
        return { k: v for k, v in self.__dict__.items() if v is not None }
    @staticmethod
    def decode(data):
        created = RecipeModel(
            _id = str(data.get('_id', False) or None),
            title = data.get('title', False) or None,
            source_url = data.get('source_url', False) or None,
            author = data.get('author', False) or None,
            total_time = data.get('total_time', False) or None,
            yields = data.get('yields', False) or None,
            image_url = data.get('image_url', False) or None,
            ingredients = data.get('ingredients', False) or None,
            instructions = data.get('instructions', False) or None,
            ratings = data.get('ratings', False) or None,
            created_at = str(data.get('created_at', False) or None),
            updated_at = str(data.get('updated_at', False) or None)
        )
        return created