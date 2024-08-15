from django.urls import path
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView, MovieStatsView


urlpatterns = [
    path('movies/', MovieCreateListView.as_view(), name='movies-create-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movies-detail-view'),
    path('movies/stats/', MovieStatsView.as_view(), name='movies-stats-view'),
]
