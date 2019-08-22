from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie,Rating
from api.serializers import MovieSerializer
from rest_framework.response import Response
from django.db.models import Avg,Count

@api_view(['GET', 'POST', 'DELETE'])
def movies(request):
   if request.method == 'GET':
       id = request.GET.get('id', request.GET.get('movie_id', None))
       title = request.GET.get('title', None)
       genre = request.GET.get('genre', None)
       order = request.GET.get('order', None)
       movies = Movie.objects.all()
       if order:
           if order == 'avgrating':
               if title:
                   movies = movies.values('id','title','genres').filter(title__icontains=title).annotate(view_cnt=Count('rating')).annotate(average_rating=Avg('rating__rating')).order_by('-average_rating')
               if genre:
                   movies = movies.values('id','title','genres').filter(genres__icontains=genre).annotate(view_cnt=Count('rating')).annotate(average_rating=Avg('rating__rating')).order_by('-average_rating')
           elif order == 'countrating':
               if title:
                   movies = movies.values('id','title','genres').filter(title__icontains=title).annotate(view_cnt=Count('rating')).annotate(average_rating=Avg('rating__rating')).order_by('-view_cnt')
               if genre:
                   movies = movies.values('id','title','genres').filter(genres__icontains=genre).annotate(view_cnt=Count('rating')).annotate(average_rating=Avg('rating__rating')).order_by('-view_cnt')
       else:
           if id:
               movies = movies.filter(pk=id)
           if title:
               movies = movies.values('id','title',"genres").filter(title__icontains=title).annotate(view_cnt=Count('rating')).annotate(average_rating=Avg('rating__rating'))
           if genre:
               movies = movies.values('id','title','genres').filter(genres__icontains=genre).annotate(view_cnt=Count('rating')).annotate(average_rating=Avg('rating__rating'))
       serializer = MovieSerializer(movies, many=True)
       return Response(data=serializer.data, status=status.HTTP_200_OK)

   if request.method == 'DELETE':
       movie = Movie.objects.all()
       movie.delete()
       return Response(status=status.HTTP_200_OK)
       
   if request.method == 'POST':
       movies = request.data.get('movies', None)
       for movie in movies:
           id = movie.get('id', None)
           title = movie.get('title', None)
           genres = movie.get('genres', None)
           if not (id and title and genres):
               continue
           if Movie.objects.filter(id=id).count() > 0 or Movie.objects.filter(title=title).count() > 0:
               continue
           Movie(id=id, title=title, genres='|'.join(genres)).save()
       return Response(status=status.HTTP_200_OK)