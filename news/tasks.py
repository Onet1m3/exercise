from celery.schedules import crontab
from exercise import celery_app
from django.utils import timezone

from .models import NewsModel
from .utils import generate_random_string


@celery_app.task
def create_periodic_news():
    title = generate_random_string(8)
    content = generate_random_string(20)
    publish_date = timezone.now()
    NewsModel.objects.create(title=title, content=content, publish_date=publish_date)