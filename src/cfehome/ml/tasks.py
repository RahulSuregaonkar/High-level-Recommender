from celery import shared_task
from . import utils as ml_utils
from movies.models import Movie
from profiles import utils as profile_utils

@shared_task
def train_surprise_model_task(n_epochs=20):
    ml_utils.train_surprise_model(n_epochs=n_epochs)
    
    
@shared_task
def batch_users_prediction_task(start_page=0, offset=250,max_pages=1000):
    model = ml_utils.load_model()
    recent_user_ids = profile_utils.get_recent_users()
    end_page = start_page + offset
    movie_ids = Movie.objects.all().popular().values_list('id',flat=True)[start_page:end_page]
    for movie_id in movie_ids:
        for u in recent_user_ids:
            pred = model.predict(uid=u,iid=movie_id).est
            print(u,movie_id,pred)
    if end_page < max_pages:
        return batch_users_prediction_task(start_page=end_page-1)
