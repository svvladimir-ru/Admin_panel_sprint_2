from django.urls import path

from movies_admin.api.v1 import views

urlpatterns = [
    path('movies', views.Movies.as_view()),  # get
    path('movies/<uuid:pk>/', views.MoviesDetailApi.as_view()),  # get
]
