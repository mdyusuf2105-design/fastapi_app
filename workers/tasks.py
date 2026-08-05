import time

from workers.celery_app import celery
from core.database import SessionLocal
from models.job import Job


@celery.task
def process_job(job_id, job_type):
    db = SessionLocal()

    try:
        job = db.query(Job).filter(Job.id == job_id).first()

        if not job:
            return

        job.status = "Running"
        db.commit()

        print(f"Processing {job_type}...")

        time.sleep(10)   # simulate long task

        job.status = "Completed"
        db.commit()

        print(f"Completed Job {job_id}")

    except Exception:
        if job:
            job.status = "Failed"
            db.commit()
        raise

    finally:
        db.close()