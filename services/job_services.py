from sqlalchemy.orm import Session
from models.job import Job
from workers.tasks import process_job



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
    process_job.delay(new_job.id, new_job.job_type)

    return new_job