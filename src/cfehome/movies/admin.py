from django.contrib import admin

# Register your models here.
from .models import Movie 

class MovieAdmin(admin.ModelAdmin):
    list_display = ['__str__','idx','calculate_ratings_count','rating_last_updated','rating_avg']
    readonly_fields = ['idx']
    search_fields = ['id']


admin.site.register(Movie, MovieAdmin)