from celery import Celery

from core.config import broker_url

celery_app = Celery("blog", broker=broker_url)
celery_app.autodiscover_tasks(["services.celery"])
