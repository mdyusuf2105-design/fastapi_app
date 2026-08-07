from sqlalchemy import func
from core.database import SessionLocal
from models.job import Job


def get_dashboard():
    db = SessionLocal()

    try:
        total_jobs = db.query(Job).count()

        pending_jobs = db.query(Job).filter(Job.status == "Pending").count()
        running_jobs = db.query(Job).filter(Job.status == "Running").count()
        completed_jobs = db.query(Job).filter(Job.status == "Completed").count()
        failed_jobs = db.query(Job).filter(Job.status == "Failed").count()

        high_jobs = db.query(Job).filter(Job.priority == "high").count()
        medium_jobs = db.query(Job).filter(Job.priority == "medium").count()
        low_jobs = db.query(Job).filter(Job.priority == "low").count()

        completed = db.query(Job).filter(
            Job.status == "Completed",
            Job.completed_at.isnot(None),
            Job.created_at.isnot(None)
        ).all()

        processing_times = [
            (job.completed_at - job.created_at).total_seconds()
            for job in completed
        ]

        average_processing_time = (
            round(sum(processing_times) / len(processing_times), 2)
            if processing_times else 0
        )

        return {
            "total_jobs": total_jobs,
            "pending_jobs": pending_jobs,
            "running_jobs": running_jobs,
            "completed_jobs": completed_jobs,
            "failed_jobs": failed_jobs,
            "average_processing_time_seconds": average_processing_time,
            "queue_statistics": {
                "high": high_jobs,
                "medium": medium_jobs,
                "low": low_jobs
            }
        }

    finally:
        db.close()