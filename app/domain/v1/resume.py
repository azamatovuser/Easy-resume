from app.crud.v1.resume import Resume as ResumeCrud
from fastapi import HTTPException

class Resume:
    def __init__(self, db):
        self.crud = ResumeCrud(db)

    def get_resume_samples(self):
        return self.crud.get_resume_samples()
    
    def add_resume_sample(self, title, image, html, css):
        self.crud.add_resume_sample(title, image, html, css)
        return HTTPException(status_code=204, detail="Created successfully")
    
    def add_resume(self, resume_request):
        self.crud.add_resume(resume_request)
        return HTTPException(status_code=204, detail="Created successfully")
    
    def add_work(self, work_request):
        self.crud.add_work(work_request)
        return HTTPException(status_code=204, detail="Created successfully")
    
    def add_education(self, education_request):
        self.crud.add_education(education_request)
        return HTTPException(status_code=204, detail="Created successfully")
    
    def add_skill(self, skill_request):
        self.crud.add_skill(skill_request)
        return HTTPException(status_code=204, detail="Created successfully")