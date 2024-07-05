""" Abstract base class for all models """
from datetime import datetime
import datetime
from typing import Any, Optional
import uuid
from abc import ABCMeta, abstractmethod
from sqlalchemy.orm import Mapped, mapped_column
from src import get_db

db = get_db()


class Base(db.Model):
    __metaclass__ = ABCMeta

    __abstract__ = True
    """
    Base Interface for all models
    """

    #id: Mapped[str] = mapped_column(db.String, primary_key=True)
    created_at: Mapped[str] = mapped_column(db.DateTime, nullable=False)
    updated_at: Mapped[str] = mapped_column(db.DateTime, nullable=False)

    def __init__(
        self,
        id = str(uuid.uuid4()),
        created_at = datetime.datetime.now(),
        updated_at = datetime.datetime.now(),
        **kwargs,
    ) -> None:
        """
        Base class constructor
        If kwargs are provided, set them as attributes
        """

        if kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    continue
                setattr(self, key, value)

        self.id = db.Column(db.String(36), primary_key=True, default=str(id or uuid.uuid4()))
        self.created_at = db.Column(db.DateTime, primary_key=False, default=created_at or db.func.current_timestamp())
        self.updated_at = db.Column(db.DateTime, primary_key=False, default=updated_at or db.func.current_timestamp())
        __mapper_args__ = {
            'polymorphic_identity': 'base',
            'polymorphic_on': self.id
        }

    @classmethod
    def get(cls, id) -> "Any | None":
        """
        This is a common method to get an specific object
        of a class by its id

        If a class needs a different implementation,
        it should override this method
        """
        from src.persistence import repo

        return repo.get(cls.__name__.lower(), id)

    @classmethod
    def get_all(cls) -> 'list["Any"]':
        """
        This is a common method to get all objects of a class

        If a class needs a different implementation,
        it should override this method
        """
        from src.persistence import repo

        return repo.get_all(cls.__name__.lower())

    @classmethod
    def delete(cls, id) -> bool:
        """
        This is a common method to delete an specific
        object of a class by its id

        If a class needs a different implementation,
        it should override this method
        """
        from src.persistence import repo

        obj = cls.get(id)

        if not obj:
            return False

        return repo.delete(obj)

    def to_dict(self) -> dict:
        """Returns the dictionary representation of the object"""

    @staticmethod
    def create(data: dict) -> Any:
        """Creates a new object of the class"""

    @staticmethod
    def update(entity_id: str, data: dict) -> 'Any | None':
        """Updates an object of the class"""
