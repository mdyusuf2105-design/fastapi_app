from pydantic import BaseModel
from enum import Enum

class JobType(str, Enum):
    file_processing = "File Processing"
    data_transformation = "Data Transformation"
    email_sending = "Email Sending Simulation"
    report_generation = "Report Generation"

class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class JobCreate(BaseModel):
    job_type: JobType
    payload: str
    priority: Priority