from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication #!fungsi autentikasi token 
from rest_framework.permissions import IsAuthenticated
from .models import Movie, Rating
from .serializer import MovieSerializer, RatingSerializer, UserSerializer
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    #!autentikasi class ini bertujan untuk mendapatkan hak akses berupa akses token
    #!dengan kode contoh token "faba811fe68bfab32066fcd8e48271c829642764" : user dapat mengakses API ini
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:

            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            # print('user:', user)

            #!kode ini bertujuan untuk meng-update rating
            #!jika rating sudah ada, maka update, jika belum ada, objek di create
            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message':'Rating updated successfully','result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message':'Rating created sucessfully', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            
        else:
            response = {'message':'You need to provide the numbers of stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
    

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)


    def create(self, reqiest, *args, **kwargs):
        response = {'message':'You cant create rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, reqiest, *args, **kwargs):
        response = {'message':'You cant update rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    



