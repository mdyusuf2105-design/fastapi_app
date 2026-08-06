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

    print(f"Sending Job {new_job.id} to queue {new_job.priority.lower()}")
    
    process_job.apply_async(
        args=[new_job.id, new_job.job_type],
        queue=new_job.priority.lower(),
        routing_key=new_job.priority.lower(),
    )

    return new_job