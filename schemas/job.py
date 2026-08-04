from pydantic import BaseModel
from enum import Enum

# Job Type Enum
class JobType(str, Enum):
    file_processing = "File Processing"
    data_transformation = "Data Transformation"
    email_sending = "Email Sending Simulation"
    report_generation = "Report Generation"

# Priority Enum
class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

# Request Schema
class JobCreate(BaseModel):
    job_type: JobType
    payload: str
    priority: Priority