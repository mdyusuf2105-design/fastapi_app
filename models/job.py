from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from core.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    job_type = Column(String(100), nullable=False)

    payload = Column(String(500), nullable=False)

    priority = Column(String(20), nullable=False)

    status = Column(String(20), default="Pending")

    retry_count = Column(Integer, default=0)

    error_message = Column(String(255), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())