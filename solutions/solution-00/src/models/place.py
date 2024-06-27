"""
Place related functionality
"""

from src.models.base import Base
from src.models.city import City
from src.models.user import User
from sqlalchemy.orm import Mapped, mapped_column
from src import get_db

db = get_db()

class Place(Base):
    __tablename__ = "places"
    """Place representation"""

    name: Mapped[str] = mapped_column(db.String, nullable=False)
    description: Mapped[str] = mapped_column(db.String, nullable=False)
    address: Mapped[str] = mapped_column(db.String, nullable=False)
    latitude: Mapped[float] = mapped_column(db.Float, nullable=False)
    longitude: Mapped[float] = mapped_column(db.Float, nullable=False)
    host_id: Mapped[str] = mapped_column(db.String, nullable=False)
    city_id: Mapped[str] = mapped_column(db.String, nullable=False)
    price_per_night: Mapped[int] = mapped_column(db.Integer, nullable=False)
    number_of_rooms: Mapped[int] = mapped_column(db.Integer, nullable=False)
    number_of_bathrooms: Mapped[int] = mapped_column(db.Integer, nullable=False)
    max_guests: Mapped[int] = mapped_column(db.Integer, nullable=False)

    def __init__(self, data: 'dict | None' = 'None', **kw) -> None:
        """Dummy init"""

        if not data:
            return

        self.name = db.Column(db.String(64), primary_key=False, nullable = False, default=data.get("name", ""))
        self.description = db.Column(db.String(1024), primary_key=False, nullable = False, default=data.get("description", ""))
        self.address = db.Column(db.String(1024), primary_key=False, nullable = False, default=data.get("address", ""))
        self.city_id = db.Column(db.String(36), db.ForeignKey('cities.id'), primary_key=False, nullable = False, default=data["city_id"])
        self.latitude = db.Column(db.Float, primary_key=False, nullable = False, default=float(data.get("latitude", 0.0)))
        self.longitude = db.Column(db.Float, primary_key=False, nullable = False, default=float(data.get("longitude", 0.0)))
        self.host_id = db.Column(db.String(36), db.ForeignKey('users.id'), primary_key=False, nullable = False, default=data["host_id"])
        self.price_per_night = db.Column(db.Integer, primary_key=False, nullable = False, default=int(data.get("price_per_night", 0)))
        self.number_of_rooms = db.Column(db.Integer, primary_key=False, nullable = False, default=int(data.get("number_of_rooms", 0)))
        self.number_of_bathrooms = db.Column(db.Integer, primary_key=False, nullable = False, default=int(data.get("number_of_bathrooms", 0)))
        self.max_guests = db.Column(db.Integer, primary_key=False, nullable = False, default=int(data.get("max_guests", 0)))

    def __repr__(self) -> str:
        """Dummy repr"""
        return f"<Place {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "city_id": self.city_id,
            "host_id": self.host_id,
            "price_per_night": self.price_per_night,
            "number_of_rooms": self.number_of_rooms,
            "number_of_bathrooms": self.number_of_bathrooms,
            "max_guests": self.max_guests,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(data: dict) -> "Place":
        """Create a new place"""
        from src.persistence import repo

        user: User | None = User.get(data["host_id"])

        if not user:
            raise ValueError(f"User with ID {data['host_id']} not found")

        city: City | None = City.get(data["city_id"])

        if not city:
            raise ValueError(f"City with ID {data['city_id']} not found")

        new_place = Place(data=data)

        repo.save(new_place)

        return new_place

    @staticmethod
    def update(place_id: str, data: dict) -> "Place | None":
        """Update an existing place"""
        from src.persistence import repo

        place: Place | None = Place.get(place_id)

        if not place:
            return None

        for key, value in data.items():
            setattr(place, key, value)

        repo.update(place)

        return place
