from app.crud.v1.feedbacks import Feedback as FeedbackCrud
from app.domain.v1.users import User as UserDomain
from fastapi import HTTPException

class Feedback:
    def __init__(self, db):
        self.crud = FeedbackCrud(db)
        self.user_domain = UserDomain(db)

    def get_feedbacks(self):
        return self.crud.get_feedbacks()
    
    def add_feedback(self, feedback_request, token):
        user_id = self.user_domain.get_user_id_from_token(token)
        self.crud.add_feedback(feedback_request, user_id)
        return HTTPException(status_code=201, detail="Created successfully")