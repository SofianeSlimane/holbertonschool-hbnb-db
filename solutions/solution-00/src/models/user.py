"""
User related functionality
"""

from src.models.base import Base
from typing import Optional, Union, List, Any
from flask_bcrypt import Bcrypt
from sqlalchemy.orm import Mapped, mapped_column
from src import get_db
import datetime
import uuid
db = get_db()
bcrypt = Bcrypt()
class User(Base):
    """User representation"""
    __tablename__ = "users"  
    
    first_name: Mapped[str] = mapped_column(db.String, nullable=False)  
    last_name: Mapped[str] = mapped_column(db.String, nullable=False)
    email: Mapped[str] = mapped_column(db.String, nullable=False)
    password: Mapped[str] = mapped_column(db.String, nullable=True)
    is_admin: Mapped[bool] = mapped_column(db.String, nullable=False)
    id: Mapped[str] = mapped_column(db.String, primary_key=True)
    def __init__(self, email: str, password: Optional[str] = None, first_name: Optional[str] = None, last_name: Optional[str] = None, **kw):
        """Initialize a new User"""
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.id = str(uuid.uuid4())
        self.is_admin = False

    def __repr__(self) -> str:
        """String representation of the User object"""
        return f"<User {self.id} ({self.email})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": str(self.id),
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
            "password": self.password
        }
    def set_password(self, password):
         return bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        user_check_pw = User.get(self.id)
        return bcrypt.check_password_hash(user_check_pw.password, password)

    @staticmethod
    def create(user: dict) -> "User":
        """Create a new user"""
        from src.persistence import repo
        #users: List[User] = User.get_all()  

        
        #for u in users:
            #if u.email == user["email"]:
                #raise ValueError("User already exists")

        new_user = User(**user)  
        new_user.password = User.set_password(new_user, new_user.password)
        repo.save(new_user) 

        return new_user

    @staticmethod
    def update(user_id: str, data: dict) -> Optional["User"]:
        """Update an existing user"""
        from src.persistence import repo

        user: Optional[User] = User.get(user_id)  

        if not user:
            return None  
        
        if "email" in data:
            user.email = data["email"]
        if "first_name" in data:
            user.first_name = data["first_name"]
        if "last_name" in data:
            user.last_name = data["last_name"]
        if "password" in data:
            user.password = data["password"]

        repo.update(user)  

        return user

    #@staticmethod
    #def get(user_id: str) -> Optional["User"]:
        #"""Retrieve a user by ID"""
        #from src.models.base import Base
        #return Base.get(cls, User, user_id)

    #@staticmethod
    #def get_all() -> List["User"]:
        #"""Retrieve all users"""
        #from src.models.base import Base
        #return Base.get_all()
