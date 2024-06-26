"""
Country related functionality
"""

from sqlalchemy import Column, String  # Import necessary SQLAlchemy components
from src.models.base import Base  # Import Base class for SQLAlchemy integration
from typing import List  # Import List type hint for type annotations


class Country(Base):
    """
    Country representation

    This class inherits from Base for SQLAlchemy integration

    This class is used to get and list countries
    """
    name: str  # Define name attribute as a string
    code: str  # Define code attribute as a string
    cities: list  # Placeholder for cities attribute (not implemented)

    __tablename__ = "countries"  # Define the table name in the database

    # Define SQLAlchemy columns for name and code
    name = Column(String(100), primary_key=True)  # Country name as primary key
    code = Column(String(3), unique=True, nullable=False)  # Country code as unique and not nullable

    def __init__(self, name: str, code: str, **kw) -> None:
       """Initialize a new Country object with name and code"""
       super().__init__(**kw)  # Call superclass constructor
       self.name = name  # Initialize name attribute
       self.code = code  # Initialize code attribute

    def __repr__(self) -> str:
        """Returns a string representation of the Country object"""
        return f"<Country {self.code} ({self.name})>"  # Return string representation of Country object

    def to_dict(self) -> dict:
        """Returns the dictionary representation of the country"""
        return {
            "name": self.name,
            "code": self.code,
        }

    @staticmethod
    def get_all() -> List["Country"]:
        """Get all countries"""
        from src.persistence import repo  # Import repo locally to avoid circular imports

        countries: list["Country"] = repo.get_all("country")  # Get all countries from repository

        return countries  # Return list of Country objects

    @staticmethod
    def get(code: str) -> "Country | None":
         """Get a country by its code"""
         for country in Country.get_all():  # Iterate over all countries
            if country.code == code:  # Check if country code matches
                return country  # Return the country object if found
         return None  # Return None if country with specified code is not found

    @staticmethod
    def create(name: str, code: str) -> "Country":
        """Create a new country"""
        from src.persistence import repo  # Import repo locally to avoid circular imports

        country = Country(name, code)  # Create a new Country object

        repo.save(country)  # Save the new country object using repository

        return country  # Return the created country object
