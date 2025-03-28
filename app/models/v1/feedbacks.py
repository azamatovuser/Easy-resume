from app.database import Base
from sqlalchemy import Column, Integer, String, func, DateTime, ForeignKey, Text
from pydantic import BaseModel, Field

class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    full_name = Column(String)
    message = Column(Text)
    stars = Column(Integer, nullable=False)
    created_date = Column(DateTime, server_default=func.now())


class FeedbackRequest(BaseModel):
    full_name: str = Field(min_length=3)
    message: str
    stars: int = Field(gt=0)