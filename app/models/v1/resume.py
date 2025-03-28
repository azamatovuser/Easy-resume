from app.database import Base
from sqlalchemy import Column, Integer, String, func, DateTime, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field
from typing import Optional, List

resume_skills = Table(
    'resume_skills',
    Base.metadata,
    Column('resume_id', Integer, ForeignKey('resumes.id'), primary_key=True),
    Column('skill_id', Integer, ForeignKey('skills.id'), primary_key=True)
)

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    skill_name = Column(String, nullable=False, unique=True)

    resumes = relationship("Resume", secondary=resume_skills, back_populates="skills")

class Work(Base):
    __tablename__ = "works"

    id = Column(Integer, primary_key=True, index=True)
    resume_id = Column(Integer, ForeignKey('resumes.id'), nullable=False)
    company_name = Column(String, nullable=True)
    position = Column(String, nullable=True)
    from_date = Column(DateTime, nullable=True)
    to_date = Column(DateTime, nullable=True)
    job_description = Column(String, nullable=True)

    resume = relationship("Resume", back_populates="works")

class Education(Base):
    __tablename__ = "educations"

    id = Column(Integer, primary_key=True, index=True)
    resume_id = Column(Integer, ForeignKey('resumes.id'), nullable=True)
    university_name = Column(String, nullable=True)
    major = Column(String, nullable=True)
    from_date = Column(Integer, nullable=True)
    to_date = Column(Integer, nullable=True)

    resume = relationship("Resume", back_populates="educations")

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="resumes")
    image = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    city = Column(String, nullable=False)
    mail = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    about = Column(String, nullable=True)

    works = relationship("Work", back_populates="resume")
    educations = relationship("Education", back_populates="resume")
    skills = relationship("Skill", secondary=resume_skills, back_populates="resumes")

class ResumeSample(Base):
    __tablename__ = "resumesamples"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    type = Column(String, nullable=False)
    image = Column(String, nullable=False)
    html = Column(String, nullable=False)
    css = Column(String, nullable=True)

class WorkRequest(BaseModel):
    resume_id: int = Field(gt=0)
    company_name: Optional[str] = None
    position: Optional[str] = None
    from_date: Optional[str] = None
    to_date: Optional[str] = None
    job_description: Optional[str] = None

class EducationRequest(BaseModel):
    resume_id: int = Field(gt=0)
    university_name: Optional[str] = None
    major: Optional[str] = None
    from_date: Optional[str] = None
    to_date: Optional[str] = None

class SkillRequest(BaseModel):
    skill_name: str

class ResumeRequest(BaseModel):
    user_id: int = Field(gt=0)
    image: str
    full_name: str
    country: str
    city: str
    mail: Optional[str] = None
    phone_number: Optional[str] = None
    about: Optional[str] = None