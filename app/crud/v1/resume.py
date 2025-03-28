from app.models.v1.resume import ResumeSample as ResumeSampleDB, Resume as ResumeDB, Work as WorkDB, Education as EducationDB, Skill as SkillDB
from app.settings import BASE_DIR
import os

class Resume:
    def __init__(self, db):
        self.db = db

    def get_resume_samples(self):
        return self.db.query(ResumeSampleDB).all()
    
    def add_resume_sample(self, title, image, html, css):
        formatted_name = title.replace(" ", "_").lower()

        os.makedirs("samples", exist_ok=True)
        os.makedirs("templates/html", exist_ok=True)
        os.makedirs("templates/css", exist_ok=True)

        image_extension = os.path.splitext(image.filename)[1]
        image_save_path = os.path.join("samples", f"{formatted_name}{image_extension}")
        with open(image_save_path, "wb") as f:
            f.write(image.file.read())

        html_save_path = os.path.join("templates/html", f"{formatted_name}.html")
        with open(html_save_path, "wb") as f:
            f.write(html.file.read())

        css_save_path = os.path.join("templates/css", f"{formatted_name}.css")
        with open(css_save_path, "wb") as f:
            f.write(css.file.read())

        resume_sample = ResumeSampleDB(
            title=title,
            type=formatted_name,
            image=image_save_path,
            html=html_save_path,
            css=css_save_path
        )
        
        self.db.add(resume_sample)
        self.db.commit()

    def add_resume(self, resume_request):
        resume = ResumeDB(
            user_id=resume_request.user_id,
            image=resume_request.image,
            full_name=resume_request.full_name,
            country=resume_request.country,
            city=resume_request.city,
            mail=resume_request.mail,
            phone_number=resume_request.phone_number,
            about=resume_request.about
        )
        self.db.add(resume)
        self.db.commit()

    def add_work(self, work_request):
        work = WorkDB(
            resume_id=work_request.resume_id,
            company_name=work_request.company_name,
            position=work_request.position,
            from_date=work_request.from_date,
            to_date=work_request.to_date,
            job_description=work_request.job_description
        )
        self.db.add(work)
        self.db.commit()

    def add_education(self, education_request):
        education = EducationDB(
            resume_id=education_request.resume_id,
            university_name=education_request.university_name,
            major=education_request.major,
            from_date=education_request.from_date,
            to_date=education_request.to_date
        )
        self.db.add(education)
        self.db.commit()

    def add_skill(self, skill_request):
        skill = SkillDB(
            skill_name=skill_request.skill_name
        )
        self.db.add(skill)
        self.db.commit()