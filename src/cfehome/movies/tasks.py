from django.db.models import Window, F
from django.db.models.functions import DenseRank


from django.apps import apps

from celery import shared_task
import logging

'''logger = logging.getLogger(__name__)
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
        raise'''
    

@shared_task
def update_movie_position_embedding_idx():
    Movie = apps.get_model('movies', "Movie")
    qs = Movie.objects.all().annotate(
        new_idx=Window(
            expression=DenseRank(),
            order_by=[F('id').asc()]
        )
    ).annotate(final_idx = F('new_idx') - 1)
    updated = 0
    for obj in qs:
        if obj.final_idx != obj.idx:
            updated += 1
            obj.idx = obj.final_idx
            obj.save()
    print(f"Updated {updated} movie idx fields")