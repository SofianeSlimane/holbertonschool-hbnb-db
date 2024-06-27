"""
User related functionality
"""

from src.models.base import Base
from sqlalchemy import Column, String, Boolean, DateTime, func
from typing import Optional, Union, List, Any


class User(Base):
    """User representation"""
    __tablename__ = "users"  # Define the name of the table associated with this model

    # Defining columns with SQLAlchemy
    first_name = Column(String(50), nullable=True)  # User's first name
    last_name = Column(String(50), nullable=True)  # User's last name
    email = Column(String(120), unique=True, nullable=False)  # Unique email address
    password = Column(String(128), nullable=False)  # User password
    is_admin = Column(Boolean, default=False)  # Indicator if user is admin

    def __init__(self, email: str, password: str, first_name: Optional[str] = None, last_name: Optional[str] = None, **kw):
        """Initialize a new User"""
        super().__init__(**kw)  # Calling the parent class constructor
        self.email = email  # Email initialization
        self.password = password  # Initialize password
        self.first_name = first_name  # First name initialization
        self.last_name = last_name  # Surname initialization
        __mapper_args__ = {
            'polymorphic_identity': 'users',
            'polymorphic_on': self.id
        }

    def __repr__(self) -> str:
        """String representation of the User object"""
        return f"<User {self.id} ({self.email})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @staticmethod
    def create(user: dict) -> "User":
        """Create a new user"""
        from src.persistence import repo
        users: List[User] = User.get_all()  # Retrieve all existing users

        # Check if the user already exists
        for u in users:
            if u.email == user["email"]:
                raise ValueError("User already exists")

        new_user = User(**user)  # Create a new user

        repo.save(new_user)  # Save the new user in the repository

        return new_user

    @staticmethod
    def update(user_id: str, data: dict) -> Optional["User"]:
        """Update an existing user"""
        from src.persistence import repo

        user: Optional[User] = User.get(user_id)  # Retrieve user by ID

        if not user:
            return None  # Return None if user does not exist

        # Update user fields
        if "email" in data:
            user.email = data["email"]
        if "first_name" in data:
            user.first_name = data["first_name"]
        if "last_name" in data:
            user.last_name = data["last_name"]
        if "password" in data:
            user.password = data["password"]

        repo.update(user)  # Update user in repository

        return user

    @staticmethod
    def get(user_id: str) -> Optional["User"]:
        """Retrieve a user by ID"""
        from src.models.base import Base
        return Base.get(user_id)

    @staticmethod
    def get_all() -> List["User"]:
        """Retrieve all users"""
        from src.models.base import Base
        return Base.get_all()
