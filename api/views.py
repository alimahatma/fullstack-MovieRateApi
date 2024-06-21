from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie, Rating
from .serializer import MovieSerialzer, RatingSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerialzer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

