"""
City related functionality
"""

from src.models.base import Base
from src.models.country import Country
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src import get_db
from datetime import datetime
import uuid
db = get_db()

class City(Base):
    """City representation"""
     
    
    id = db.Column(db.String(36), primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())
    name = db.Column(db.String, db.ForeignKey('country.name'))
    country_code = db.Column(db.String(10), db.ForeignKey('country.code'))

    def __init__(self, name: str, country_code: str, **kw) -> None:
        """Dummy init"""
        self.name = name
        self.country_code = country_code
        self.created_at = datetime.now
        self.update_at = datetime.now
        self.id = uuid.uuid4()
    def __repr__(self) -> str:
        """Dummy repr"""
        return f"<City {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "country_code": self.country_code,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
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

        #city = City.get(city_id)
        city = City.query.filter(City.id == city_id).update(data)
        if not city:
            raise ValueError("City not found")
            
        #else:
            #for key, value in data.items():
                #setattr(city, key, value)

        repo.update(city)

        return city
