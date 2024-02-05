from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from .models import Rating
from django.views.decorators.http import require_http_methods

@require_http_methods(['POST'])
def rate_movie_view(request):
    print(request.POST)
    if not request.htmx:
        return HttpResponse("Not Allowed Method", status=400 )
    object_id = request.POST.get('object_id')
    print(f"object_id={object_id}")
    rating_value= request.POST.get('rating_value')
    if object_id is None or rating_value is None:
        response = HttpResponse("Skipping", status=200)
        response['HX-Trigger'] = 'did-skip-movie'
        return response
    user = request.user
    message = "you must <a href='/accounts/login/'>login</a> to rate this."
    if user.is_authenticated:
        message = "<span class='bg-danger text-light py-1 px-3 rounded'>An error occured.</div>"
        ctype = ContentType.objects.get(app_label='movies', model='movie')
        rating_obj = Rating.objects.create(content_type=ctype, object_id=object_id, value=rating_value, user=user)
        if rating_obj.content_object is not None:
            message = "<span class='bg-success text-light py-1 px-3 rounded'>Rating saved!</div>"
            response = HttpResponse("Skipping", status=200)
            response['HX-Trigger-After-Settle'] = 'did-rate-movie'
            return response
            
    return HttpResponse(message, status=200)