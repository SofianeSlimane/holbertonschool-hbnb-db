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

#from src.models.base import Base
#from src.persistence.repository import Repository
#from utils.constants import FILE_STORAGE_FILENAME
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)



class DBRepository(Repository):
    """Dummy DB repository"""
    __filename = FILE_STORAGE_FILENAME
    __data: dict[str, list] = {
        "country": [],
        "user": [],
        "amenity": [],
        "city": [],
        "review": [],
        "place": [],
        "placeamenity": [],
    }

    def __init__(self) -> None:
        """Not implemented"""


    def get_all(self, model_name: str) -> list:
        """Not implemented"""
        return model_name.query.all()

    def get(self, model_name: str, obj_id: str) -> Base | None:
        # Retrieves object in database based on its id
        return model_name.query.filter(id == obj_id).first()


    def reload(self) -> None:
        """Not implemented"""
        self.reload


    def save(self, obj) -> None:
        """Not implemented"""
        if app.config['USE_DATABASE']:
             db.session.add(obj)
             db.session.commit()
        else:
            # Implement file-based save logic
            self.__data[obj.__class__.__name__.lower()].append(obj)
            with open(self.__filename, "w") as file:
                json.dump(DBRepository.__data, file)

    def update(self, obj: Base) -> Base | None:
        """Not implemented"""

    def delete(self, obj: Base) -> bool:
        """Not implemented"""
        return False
