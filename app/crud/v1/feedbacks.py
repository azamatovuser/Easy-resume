from app.models.v1.feedbacks import Feedback as FeedbackDB

class Feedback:
    def __init__(self, db):
        self.db = db

    def get_feedbacks(self):
        return self.db.query(FeedbackDB).all()
    
    def add_feedback(self, feedback_request, user_id):
        feedback = FeedbackDB(
            user_id=user_id,
            full_name=feedback_request.full_name,
            message=feedback_request.message,
            stars=feedback_request.stars
        )
        self.db.add(feedback)
        self.db.commit()