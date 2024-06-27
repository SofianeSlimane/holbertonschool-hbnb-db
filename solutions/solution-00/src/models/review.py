"""
Review related functionality
"""

from src.models.base import Base
from src.models.place import Place
from src.models.user import User
from sqlalchemy.orm import Mapped, mapped_column
from src import get_db
import uuid

db = get_db()

class Review(Base):
    __tablename__ = "reviews"
    """Review representation"""
    target_place_id: Mapped[str] = mapped_column(db.ForeignKey("places.id"), nullable=False, use_existing_column=True)
    user_id: Mapped[str] = mapped_column(db.ForeignKey("users.id"), nullable=False)
    comment: Mapped[str] = mapped_column(db.String, nullable=False)
    rating: Mapped[float] = mapped_column(db.Float, nullable=False)

    def __init__(
        self, place_id: str, user_id: str, comment: str, rating: float, **kw
    ) -> None:
        """Dummy init"""
        super().__init__(**kw)

        self.target_place_id = db.Column(db.String(36), db.ForeignKey('places.id'), primary_key=False, nullable = False, default=place_id)
        self.user_id = db.Column(db.String(36), db.ForeignKey('users.id'), primary_key=False, nullable = False, default=user_id)
        self.comment = db.Column(db.String(1024), primary_key=False, nullable = False, default=comment) 
        self.rating = db.Column(db.Float, primary_key=False, nullable = False, default=rating)
        __mapper_args__ = {
            'polymorphic_identity': 'reviews',
            'polymorphic_on': self.id
        }

    def __repr__(self) -> str:
        """Dummy repr"""
        return f"<Review {self.id} - '{self.comment[:25]}...'>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "place_id": self.target_place_id,
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
