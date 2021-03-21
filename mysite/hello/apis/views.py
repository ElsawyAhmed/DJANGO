from rest_framework import viewsets
from .. models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

class MovieAPI(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


@api_view(['GET'])
def listAll(request):
    moviesList = Movie.objects.all()
    serializer = MovieSerializer(instance = moviesList, many = True)
    return Response(data = serializer.data, status = status.HTTP_200_OK)


@api_view(['DELETE','GET'])
def delete_movie(request, Id):
    movie = Movie.objects.get(pk=Id)
    if movie:
        movie.delete()
        return Response(status = status.HTTP_200_OK)

# @api_view(['PUT','GET'])
# def update_movie(request, Id):
#     movie = Movie.objects.get(pk=Id)
#     if movie:
#         movie.delete()
#         return Response(status = status.HTTP_200_OK)

@api_view(['POST',])
def add_movie(request):
    movie = MovieSerializer(data = request.data)
    if movie.is_valid():
        movie.save()
        return Response(data = {
            'success':True,
            'massage':'Movie Added Successfuly'
        },status = status.HTTP_201_CREATED)
    return Response(data = {
        'success':False,
        'errros':movie.errors,
        'massage':'Problem Happened May be Your data Not Valid'
    },status = status.HTTP_400_BAD_REQUEST)