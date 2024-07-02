"""
  Now is easy to implement the database repository. The DBRepository
  should implement the Repository (Storage) interface and the methods defined
  in the abstract class Storage.

  The methods to implement are:
    - get_all
    - get
    - save
    - update
    - delete
    - reload (which can be empty)
"""

from src.models.base import Base
from src.persistence.repository import Repository
from src import get_db, create_app
from utils.constants import REPOSITORY_ENV_VAR
from src import create_app
import os
from src.models.user import User
from src.models.country import Country
from utils.populate import populate_db
from src.models.amenity import Amenity
from src.models.city import City
from src.models.place import Place
from src.models.review import Review
db = get_db()
class DBRepository(Repository):
    """Dummy DB repository"""
    
    def __init__(self) -> None:
        """Not implemented"""
        self.reload()

    def get_all(self, model_name: str) -> list:
        """Not implemented"""
        if model_name == "user":
            users_list = User.query.all()
            return users_list
        elif model_name == "country":
            country_list = Country.query.all()
            return country_list
        elif model_name == "amenity":
            amenity_list = Amenity.query.all()
            return amenity_list
        elif model_name == "city":
            city_list = City.query.all()
            return city_list
        elif model_name == "place":
            places_list = Place.query.all()
            return places_list
        elif model_name == "review":
            review_list = Review.query.all()
            return review_list

    def get(self, model_name: str, obj_id: str) -> Base | None:
        """Not implemented"""
        if model_name == "user":
            user_by_id = User.query.filter_by(id=obj_id).first()
            return user_by_id
        elif model_name == "country":
            country_by_code = Country.query.filter_by(code=obj_id).first()
            return country_by_code
        elif model_name == "amenity":
            amenity_by_id = Amenity.query.filter_by(id=obj_id).first()
            return amenity_by_id
        elif model_name == "city":
            city_by_id = City.query.filter_by(id=obj_id).first()
            return city_by_id
        elif model_name == "place":
            place_by_id = Place.query.filter_by(id=obj_id).first()
            return place_by_id
        elif model_name == "review":
            review_by_id = Review.query.filter_by(id=obj_id).first()
            return review_by_id

    def reload(self) -> None:
        """Not implemented"""
        populate_db(self)

    def save(self, obj) -> None:
        """Not implemented"""
        db.session.add(obj)
        db.session.commit()
        





    def update(self, obj: Base) -> Base | None:
        """Not implemented"""
        db.session.commit()

    def delete(self, obj: Base) -> bool:
        """Not implemented"""
        db.session.delete(obj)
        db.session.commit()
        return True
    
