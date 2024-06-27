"""
Country related functionality
"""
from typing import Any
from src import get_db
from src.models.base import Base
from datetime import datetime
import uuid
db = get_db()

from sqlalchemy import Column, String  # Import necessary SQLAlchemy components
from src.models.base import Base  # Import Base class for SQLAlchemy integration
from typing import List, Optional  # Import List and Optional type hints for type annotations
from abc import ABC, abstractmethod  # Import ABC and abstractmethod for abstract class functionality

<<<<<<< HEAD
class Country(Base):
=======

class Country(Base, ABC):
>>>>>>> 0f7f5518d67686a3922df33462ac7d941d5fe995
    """
    Country representation

    This class inherits from Base for SQLAlchemy integration

    This class is used to get and list countries
    """
    __tablename__ = "countries"  # Define the table name in the database

<<<<<<< HEAD
    name = db.Column(db.String(58), unique=True)
    code = db.Column(db.String(58), unique=True)
    cities = db.Column(db.String(500), unique=True)
    id = db.Column(db.String(58), primary_key=True)
    def __init__(self, name: str, code: str, **kw) -> None:
        """Dummy init"""
        self.name = name
        self.code = code
        self.created_at = datetime.now
        self.update_at = datetime.now
        self.id = uuid.uuid4()
=======
    # Define SQLAlchemy columns for name and code
    name = Column(String(100), primary_key=True)  # Country name as primary key
    code = Column(String(3), unique=True, nullable=False)  # Country code as unique and not nullable

    def __init__(self, name: str, code: str, **kw) -> None:
        """Initialize a new Country object with name and code"""
        super().__init__(**kw)  # Call superclass constructor
        self.name = name  # Initialize name attribute
        self.code = code  # Initialize code attribute
>>>>>>> 0f7f5518d67686a3922df33462ac7d941d5fe995

    def __repr__(self) -> str:
        """Returns a string representation of the Country object"""
        return f"<Country {self.code} ({self.name})>"  # Return string representation of Country object

    def to_dict(self) -> dict:
        """Returns the dictionary representation of the country"""
        return {
            "name": self.name,
            "code": self.code,
        }

    @classmethod
    def get_all(cls) -> List["Country"]:
        """Get all countries"""
        from src.persistence import repo  # Import repo locally to avoid circular imports

        countries: list["Country"] = repo.get_all(cls.__name__.lower())  # Get all countries from repository

        return countries  # Return list of Country objects

    @classmethod
    def get(cls, code: str) -> Optional["Country"]:
        """Get a country by its code"""
        from src.persistence import repo  # Import repo locally to avoid circular imports

        country: Optional["Country"] = repo.get(cls.__name__.lower(), code)  # Get the country by code from repository
        return country  # Return the country object if found, else None

    @staticmethod
    def create(name: str, code: str) -> "Country":
        """Create a new country"""
        from src.persistence import repo  # Import repo locally to avoid circular imports

        country = ConcreteCountry(name, code)  # Create a new ConcreteCountry object

        repo.save(country)  # Save the new country object using repository

<<<<<<< HEAD
        return country
    @staticmethod
    def update(entity_id: str, data: dict) -> Any | None:
        pass
=======
        return country  # Return the created country object

    @abstractmethod
    def update(self):
        """Abstract method to update the country"""
        pass  # This method should be implemented by subclasses


class ConcreteCountry(Country):
    def __init__(self, name: str, code: str, **kw) -> None:
        """Initialize a new ConcreteCountry object with name and code"""
        super().__init__(name, code, **kw)  # Call superclass constructor

    def update(self):
        """Implementation of the abstract update method"""
        # Add the actual update logic here
        print(f"Updating country {self.name}")
>>>>>>> 0f7f5518d67686a3922df33462ac7d941d5fe995
