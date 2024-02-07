from django.shortcuts import render
from movies.models import Movie
from suggestions.models import Suggestion

# Create your views here.
def home_view(request):
    context = {}
    user = request.user
    top_popular = Movie.objects.all().popular().order_by("?")
    top_popular_1 = top_popular[0]
    top_popular_2 = top_popular[1]
    top_popular_3 = top_popular[2]
    top_popular_4 = top_popular[3]
    qs_home = Movie.objects.all().popular()[6:25]
    if not user.is_authenticated:
        context['top_popular_1']=top_popular_1
        context['top_popular_2']=top_popular_2
        context['top_popular_3']=top_popular_3
        context['top_popular_4']=top_popular_4
        context['object_list'] = qs_home
        return render(request, 'home.html', context)
    context['endless_path'] = '/'
    suggestion_qs = Suggestion.objects.filter(user=user, did_rate=False)
    max_movie = 16
    request.session['total-new-suggestions'] = suggestion_qs.count()
    if suggestion_qs.exists():
        movie_ids = suggestion_qs.order_by('-value').values_list('object_id',flat=True)
        qs = Movie.objects.by_id_order(movie_ids)
        context['object_list'] = qs[:max_movie]
    else:
        context['object_list'] = Movie.objects.all().order_by("?")[:max_movie]
    
    context['top_popular_1']=top_popular_1
    context['top_popular_2']=top_popular_2
    context['top_popular_3']=top_popular_3
    context['top_popular_4']=top_popular_4
    if request.htmx:
        return render(request, "movies/snippet/infinite.html")
    return render(request, "dashboard/main.html", context)