from fastapi import FastAPI
from app.database import Base, engine
from app.routers.v1.users import router as users_router
from app.routers.v1.feedbacks import router as feedbacks_router
from app.routers.v1.resume import router as resume_router

app = FastAPI()

app.include_router(users_router, prefix="/users", tags=["User"])
app.include_router(feedbacks_router, prefix="/feedbacks", tags=["Feedback"])
app.include_router(resume_router, prefix="/resume", tags=["Resume"])

@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)