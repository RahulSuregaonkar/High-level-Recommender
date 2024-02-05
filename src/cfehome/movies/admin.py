from django.contrib import admin

# Register your models here.
from .models import Movie 

class MovieAdmin(admin.ModelAdmin):
    list_display = ['__str__','calculate_ratings_count','rating_last_updated','rating_avg']
    readonly_fields = ['rating_avg_display','rating_avg','rating_count']
    search_fields = ['id']


admin.site.register(Movie, MovieAdmin)