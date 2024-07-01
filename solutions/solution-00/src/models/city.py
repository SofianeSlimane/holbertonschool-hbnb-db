"""
City related functionality
"""

from src.models.base import Base
from src.models.country import Country
from sqlalchemy.orm import Mapped, mapped_column
from src import get_db
import datetime
import uuid
db = get_db()

class City(Base):
    """City representation"""
    __tablename__ = "cities"
    
    name: Mapped[str] = mapped_column(db.String, nullable=False)
    country_code: Mapped[str] = mapped_column(db.String, db.ForeignKey('countries.code'), nullable=False)
    id: Mapped[str] = mapped_column(db.String, primary_key=True)
    def __init__(self, name: str, country_code: str, **kw) -> None:
        """Dummy init"""
        self.name = name
        self.country_code = country_code
        self.created_at = str(datetime.datetime.now())
        self.updated_at = str(datetime.datetime.now())
        self.id = str(uuid.uuid4())
    
    
    def __repr__(self) -> str:
        """Dummy repr"""
        return f"<City {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "country_code": self.country_code,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @staticmethod
    def create(data: dict) -> "City":
        """Create a new city"""
        from src.persistence import repo

        country = Country.get(data["country_code"])

        if not country:
            raise ValueError("Country not found")

        city = City(**data)
        repo.save(city)
        return city

    @staticmethod
    def update(city_id: str, data: dict) -> "City":
        """Update an existing city"""
        from src.persistence import repo

        city = City.get(city_id)
        for key, value in data.items():
            setattr(city, key, value)

        repo.update(city)

        return city
