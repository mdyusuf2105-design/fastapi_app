from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.job import Job
from schemas.job import JobCreate
from services.job_services import create_job
from core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_new_job(job: JobCreate,
                   db: Session = Depends(get_db)):
    return create_job(db, job)

@router.get("/")
def get_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()