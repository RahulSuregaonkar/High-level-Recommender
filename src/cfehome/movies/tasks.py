

from .models import Movie


from celery import shared_task
import logging

logger = logging.getLogger(__name__)
@shared_task(name="task_calculate_movie_ratings")
def task_calculate_movie_ratings(all=False, count=None):
    try:
        logger.info("Calculating movie ratings task started...")
        qs = Movie.objects.needs_updating()
        if all:
            qs = Movie.objects.all()
        qs = qs.order_by('rating_last_updated')
        if isinstance(count, int):
            qs = qs[:count]
        for obj in qs:
            obj.calculate_rating(save=True)
        logger.info("Calculating movie ratings task completed successfully.")
    except Exception as e:
        logger.error(f"Error in calculating movie ratings: {e}")
        raise
    

