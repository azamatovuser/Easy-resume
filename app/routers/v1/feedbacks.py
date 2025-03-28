from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from app.database import get_db
from sqlalchemy.orm import Session
from app.domain.v1.feedbacks import Feedback as FeedbackDomain
from app.models.v1.feedbacks import FeedbackRequest

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

@router.get("/all-feedbacks")
async def all_feedbacks(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    domain = FeedbackDomain(db)
    return domain.get_feedbacks()

@router.post("/add-feedback")
async def add_feedback(feedback_request: FeedbackRequest, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    domain = FeedbackDomain(db)
    return domain.add_feedback(feedback_request, token)