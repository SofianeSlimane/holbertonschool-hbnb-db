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
from src import get_db
db = get_db()


class DBRepository(Repository):
    """Dummy DB repository"""
    
    def __init__(self) -> None:
        """Not implemented"""

    def get_all(self, model_name: str) -> list:
        """Not implemented"""
        return []

    def get(self, model_name: str, obj_id: str) -> Base | None:
        """Not implemented"""

    def reload(self) -> None:
        """Not implemented"""

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
        return False