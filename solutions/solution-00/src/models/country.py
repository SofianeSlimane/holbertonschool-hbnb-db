"""
Country related functionality
"""
from typing import Any
from src import get_db
from src.models.base import Base
import datetime
import uuid
db = get_db()

from sqlalchemy import Column, String  
from src.models.base import Base  
from typing import List, Optional  
from abc import ABC, abstractmethod  
from sqlalchemy.orm import Mapped, mapped_column

class Country(Base):

    
    __tablename__ = "countries"  
    code: Mapped[str] = mapped_column(db.String, primary_key=True, default='Unknown')
    name: Mapped[str] = mapped_column(db.String, primary_key=True)

    def __init__(self, name: str, code: str, **kw) -> None:
        """Dummy init"""
        self.name = name
        self.code = code
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __repr__(self) -> str:
        """Returns a string representation of the Country object"""
        return f"<Country {self.code} ({self.country_name})>"  

    def to_dict(self) -> dict:
        """Returns the dictionary representation of the country"""
        return {
            "name": self.name,
            "code": self.code,
        }

    @classmethod
    def get(cls, code: str) -> Optional["Country"]:
        """Get a country by its code"""
        from src.persistence import repo  

        country: Optional["Country"] = repo.get(cls.__name__.lower(), code)  
        return country  

    @abstractmethod
    def update(self):
        """Abstract method to update the country"""
        pass