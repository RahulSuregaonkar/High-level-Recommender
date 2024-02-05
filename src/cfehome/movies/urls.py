from django.contrib import admin
from django.urls import path

from .import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list_view, name="home"),
    path('infinite/', views.movie_infinite_rating_view, name="infinite"),
    path('popular/', views.movie_popular_view, name="popular"),
    path('<int:pk>/', views.movie_detailed_view, name="getting_absolute_url"),
]
