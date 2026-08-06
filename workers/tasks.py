import time

from workers.celery_app import celery
from core.database import SessionLocal
from models.job import Job


@celery.task(bind=True, max_retries=3)
def process_job(self, job_id, job_type):
    db = SessionLocal()
    job = None

    try:
        job = db.query(Job).filter(Job.id == job_id).first()

        if not job:
            return

        job.status = "Running"
        db.commit()

        print(f"Processing {job_type}...")

        time.sleep(20)

        job.status = "Completed"
        db.commit()

        print(f"Completed Job {job_id}")

    except Exception as exc:
        if self.request.retries < self.max_retries:
            if job:
                job.retry_count = self.request.retries
                db.commit()

            raise self.retry(exc=exc, countdown=5)

        if job:
            job.retry_count = self.max_retries
            job.status = "Failed"
            db.commit()

        raise

    finally:
        db.close()