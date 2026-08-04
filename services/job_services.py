from sqlalchemy.orm import Session
from models.job import Job

def create_job(db: Session, job):

    new_job = Job(
        job_type=job.job_type,
        payload=job.payload,
        priority=job.priority,
        status="Pending"
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job