from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie, Rating, Profile, Person, Directors, Writers, Casts
from api.serializers import MovieSerializer, MovieDetailSerializer
from rest_framework.response import Response
from django.db.models import Avg, Count
import random


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def movies(request):
    if request.method == 'GET':
        id = request.GET.get('id', request.GET.get('movie_id', None))
        title = request.GET.get('title', None)
        genre = request.GET.get('genre', None)
        order = request.GET.get('order', None)
        age = request.GET.get('age', None)
        gender = request.GET.get('gender', None)
        occupation = request.GET.get('occupation', None)
        movies = Movie.objects.all()

        if age or gender or occupation:
            profile = Profile.objects.all()
            profile = profile.values('id')
            if age:
                if age == '10':
                    profile = profile.filter(age__lt=18)
                elif age == '20':
                    profile = profile.filter(age__range=(19, 28))
                elif age == '30':
                    profile = profile.filter(age__range=(39, 48))
                elif age == '40':
                    profile = profile.filter(age__range=(39, 48))
                elif age == '50':
                    profile = profile.filter(age__gt=49)
            if gender:
                if gender == 'M':
                    profile = profile.filter(gender='M')
                elif gender == 'F':
                    profile = profile.filter(gender='F')
            if occupation:
                profile = profile.filter(occupation__icontains=occupation)
            movies = movies.filter(rating__userid__in=profile)
        if not (id or title or genre or order or age or gender or occupation):
            print("============")
            movienum = []
            for movie in movies:
                movienum.append(movie.id)
            rand = random.sample(movienum, 10)
            movies = movies.filter(pk__in=rand)
        movies = movies.annotate(view_cnt=Count('rating')).annotate(average_rating=Avg('rating__rating'))
        if id:
            movies = movies.filter(pk=id)
        if title:
            movies = movies.filter(title__icontains=title)
        if genre:
            movies = movies.filter(genres__icontains=genre)
        if order:
            if order == 'avgrating':
                movies = movies.order_by('-average_rating')
            elif order == 'countrating':
                movies = movies.order_by('-view_cnt')

        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        movieid = request.GET.get('id', None)
        if movieid:
            movie = Movie.objects.get(pk=movieid)
            movie.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'PUT':
        id = request.GET.get('id', None)
        title = request.GET.get('title', None)
        genres = request.GET.get('genres', None)
        movies = request.data.get('movies', None)
        for movie in movies:
            id = movie.get('id', None)
            title = movie.get('title', None)
            genres = movie.get('genres', None)
            Movie.objects.filter(pk=id).update(title=title, genres='|'.join(genres))
        if id:
            Movie.objects.filter(pk=id).update(title=title, genres=genres)
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


@api_view(['GET'])
def moviedetail(request):
    id = request.GET.get('id')
    movie = Movie.objects.filter(pk=id)
    serializer = MovieDetailSerializer(movie, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)