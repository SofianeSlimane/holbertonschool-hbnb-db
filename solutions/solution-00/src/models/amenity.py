"""
Amenity related functionality
"""
from src.models.base import Base
from src.models.city import City
from src.models.user import User
from src.models.place import Place
from sqlalchemy.orm import Mapped, mapped_column
from src import get_db

db = get_db()


class Amenity(Base):
    __tablename__ = "amenities"
    """Table representation of Amenity"""
    amentity_name: Mapped[str] = mapped_column(db.String, nullable=False)
    
    
    
    def __init__(self, data: 'dict | None' = 'None', **kw) -> None:
        """Dummy init"""
        super().__init__(**kw)

        if not data:
            return
        
        self.amenity_name = db.Column(db.String(64), primary_key=False, nullable = False, default=data.get("name", ""))

    def __repr__(self) -> str:
        return f"<Amenity {self.id} ({self.amenity_name})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.amenity_name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
        

    @staticmethod
    def create(data: dict) -> "Amenity":
        """Create a new amenity"""
        
        from src.persistence import repo

        amenity = Amenity(data)    
        repo.save(amenity)
        return amenity

    @staticmethod
    def update(amenity_id: str, data: dict) -> "Amenity | None":
        """Update an existing amenity"""
        from src.persistence import repo
    
        amentity_to_update = Amenity.get(amenity_id)
        for key, value in data.items():
            setattr(amentity_to_update, key, value)
    

        repo.update(amentity_to_update)

        return amentity_to_update














class PlaceAmenity(Base):
    """PlaceAmenity representation"""

    place_id: Mapped[str] = mapped_column(db.String, nullable=False)
    amenity_id: Mapped[str] = mapped_column(db.String, nullable=False)
    
    def __init__(self, place_id: str, amenity_id: str, **kw) -> None:
        """Dummy init"""
        super().__init__(**kw)
        if len(place_id) is not 36 and len(amenity_id) is not 36:
            raise ValueError("Enter valid id")
        self.place_id = db.Column(db.String(36), db.ForeignKey('place.id'), primary_key=False, nullable = False)
        self.amenity_id = db.Column(db.String(36), db.ForeignKey('amenities.id'), primary_key=False, nullable = False)

    def __repr__(self) -> str:
        """Dummy repr"""
        return f"<PlaceAmenity ({self.place_id} - {self.amenity_id})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "place_id": self.place_id,
            "amenity_id": self.amenity_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

   
        
    @staticmethod
    def create(data: dict) -> "PlaceAmenity":
        """Create a new PlaceAmenity object"""
        from src.persistence import repo

        new_place_amenity = PlaceAmenity(**data)    
        repo.save(new_place_amenity)
        return new_place_amenity

    @staticmethod
    def update(entity_id: str, data: dict):
        """Not implemented, isn't needed"""
        raise NotImplementedError(
            "This method is defined only because of the Base class"
        )





