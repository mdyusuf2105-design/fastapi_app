from celery import Celery
from kombu import Queue

celery = Celery(
    "job_worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["workers.tasks"],
)

celery.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,

    task_default_queue="medium",

    task_default_exchange="jobs",
    task_default_exchange_type="direct",
    task_default_routing_key="medium",

    task_queues=(
        Queue("high", routing_key="high"),
        Queue("medium", routing_key="medium"),
        Queue("low", routing_key="low"),
    ),
)