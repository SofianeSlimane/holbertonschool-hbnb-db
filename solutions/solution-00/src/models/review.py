"""
Review related functionality
"""

from src.models.base import Base
from src.models.place import Place
from src.models.user import User
from datetime import datetime
from src import get_db
import uuid

db = get_db()

class Review(Base):
    """Review representation"""

    place_id = db.Column(db.String(58), db.ForeignKey('place.id'), unique=True)
    user_id = db.Column(db.String(58), db.ForeignKey('user.id'), unique=True)
    comment = db.Column(db.String(58), unique=True)
    rating = db.Column(db.String(58), unique=True)
    id = db.Column(db.String(58), primary_key=True)
    def __init__(
        self, place_id: str, user_id: str, comment: str, rating: float, **kw
    ) -> None:
        """Dummy init"""
        
        self.place_id = place_id
        self.user_id = user_id
        self.comment = comment
        self.rating = rating
        self.created_at = str(datetime.now)
        self.update_at = str(datetime.now)
        self.id = str(uuid.uuid4())
    def __repr__(self) -> str:
        """Dummy repr"""
        return f"<Review {self.id} - '{self.comment[:25]}...'>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "place_id": self.place_id,
            "user_id": self.user_id,
            "comment": self.comment,
            "rating": self.rating,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(data: dict) -> "Review":
        """Create a new review"""
        from src.persistence import repo

        user: User | None = User.get(data["user_id"])

        if not user:
            raise ValueError(f"User with ID {data['user_id']} not found")

        place: Place | None = Place.get(data["place_id"])

        if not place:
            raise ValueError(f"Place with ID {data['place_id']} not found")

        new_review = Review(**data)

        repo.save(new_review)

        return new_review

    @staticmethod
    def update(review_id: str, data: dict) -> "Review | None":
        """Update an existing review"""
        from src.persistence import repo

        review = Review.get(review_id)

        if not review:
            raise ValueError("Review not found")

        for key, value in data.items():
            setattr(review, key, value)

        repo.update(review)

        return review
