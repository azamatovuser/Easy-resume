from fastapi import APIRouter, Depends, UploadFile, File, Form
from app.domain.v1.resume import Resume as ResumeDomain
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from app.models.v1.resume import ResumeRequest, WorkRequest, SkillRequest, EducationRequest

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

@router.get("/all-resume-samples")
async def all_resume_samples(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    domain = ResumeDomain(db)
    return domain.get_resume_samples()

@router.post("/add-resume-sample")
async def add_resume_sample(
    title: str = Form(...),
    image: UploadFile = File(...), 
    html: UploadFile = File(...),
    css: UploadFile = File(),
    token: str = Depends(oauth2_scheme), 
    db: Session = Depends(get_db)
):
    domain = ResumeDomain(db)
    return domain.add_resume_sample(title, image, html, css)


@router.post("/add-resume")
async def add_resume(resume_request: ResumeRequest, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    domain = ResumeDomain(db)
    return domain.add_resume(resume_request)


@router.post("/add-work")
async def add_work(work_request: WorkRequest, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    domain = ResumeDomain(db)
    return domain.add_work(work_request)


@router.post("/add-education")
async def add_education(education_request: EducationRequest, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    domain = ResumeDomain(db)
    return domain.add_education(education_request)


@router.post("/add-skill")
async def add_skill(skill_request: SkillRequest, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    domain = ResumeDomain(db)
    return domain.add_skill(skill_request)