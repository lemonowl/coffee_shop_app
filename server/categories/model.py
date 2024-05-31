from pymongo.collection import Collection
from pymongo.cursor import Cursor
from database import DatabaseModel

__all__ = ['categories_model']


class CategoriesModel(DatabaseModel):

    @property
    def collection(self) -> Collection:
        return self.db.categories

    def get_all(self) -> Cursor:
        return self.collection.find({}, {'_id': 0})


categories_model = CategoriesModel()
