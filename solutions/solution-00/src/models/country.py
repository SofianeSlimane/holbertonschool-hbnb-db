"""
Country related functionality
"""
from typing import Any
from src import get_db
from src.models.base import Base
from datetime import datetime
import uuid
db = get_db()


class Country(Base):
    """
    Country representation

    This class does NOT inherit from Base, you can't delete or update a country

    This class is used to get and list countries
    """

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

    def __repr__(self) -> str:
        """Dummy repr"""
        return f"<Country {self.code} ({self.name})>"

    def to_dict(self) -> dict:
        """Returns the dictionary representation of the country"""
        return {
            "name": self.name,
            "code": self.code,
        }

    @staticmethod
    def get_all() -> 'list["Country"]':
        """Get all countries"""
        from src.persistence import repo

        countries: list["Country"] = repo.get_all("country")

        return countries

    @staticmethod
    def get(code: str) -> "Country | None":
        """Get a country by its code"""
        for country in Country.get_all():
            if country.code == code:
                return country
        return None

    @staticmethod
    def create(name: str, code: str) -> "Country":
        """Create a new country"""
        from src.persistence import repo

        country = Country(name, code)

        repo.save(country)

        return country
    @staticmethod
    def update(entity_id: str, data: dict) -> Any | None:
        pass
