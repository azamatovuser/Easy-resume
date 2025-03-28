from app.database import Base
from sqlalchemy import Column, Integer, String, func, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    resumes = relationship("Resume", back_populates="user")
    is_active = Column(Boolean, default=True)
    created_date = Column(DateTime, server_default=func.now())


class UserRequest(BaseModel):
    username: str = Field(min_length=3)
    password: str = Field(min_length=6)
    confirm_password: str = Field(min_length=6)


class Token(BaseModel):
    access_token: str
    token_type: str