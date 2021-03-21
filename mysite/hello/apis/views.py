from rest_framework import viewsets
from .. models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics

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
#     movie = Movie.objects.get(Id=Id)
#     print(movie)
#     serializer = MovieSerializer(instance=movie,data=request.data)
#     if serializer.is_valid():
#         serializer.save()

#         return Response(dtat = {
#             'success':True,
#             'message':'Updated Successfully'
#         },status=status.HTTP_200_OK)
    
#     return Response(data={
#         'success':False,
#         'message':'Error Happened while update',
#         'errors':serializer.errors
#     },status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST',])
def add_movie(request):
    movie = MovieSerializer(data=request.data)
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

class GenericUpdate(generics.UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class GenericDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer