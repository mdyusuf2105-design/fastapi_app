import time
from datetime import datetime

from workers.celery_app import celery
from core.database import SessionLocal
from models.job import Job
from core.logger import logger


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

        logger.info(f"Processing Job {job_id} ({job_type})")

        time.sleep(20)

        job.status = "Completed"
        job.completed_at = datetime.utcnow()

        db.commit()

        logger.info(f"Completed Job {job_id}")
        
    except Exception as exc:
        if self.request.retries < self.max_retries:
            if job:
                job.retry_count = self.request.retries
                db.commit()

            logger.warning(
                f"Retry {self.request.retries + 1} for Job {job_id}"
            )

            raise self.retry(exc=exc, countdown=5)

        if job:
            job.retry_count = self.max_retries
            job.status = "Failed"
            job.error_message = str(exc)
            db.commit()

        logger.error(
            f"Job {job_id} failed after {self.max_retries} retries"
        )

        raise

    finally:
        db.close()