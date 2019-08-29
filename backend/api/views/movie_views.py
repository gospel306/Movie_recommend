from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie, Rating, Profile
from api.serializers import MovieSerializer, RankSerializer
from rest_framework.response import Response
from django.db.models import Avg, Count, Subquery


@api_view(['GET', 'POST', 'DELETE', 'UPDATE'])
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
                elif genre:
                    movies = movies.values('id','title','genres').filter(genres__icontains=genre).annotate(view_cnt=Count('rating')).annotate(average_rating=Avg('rating__rating')).order_by('-average_rating')
                else:
                    movies = movies.values('id', 'title', 'genres').annotate(view_cnt=Count('rating')).annotate(average_rating=Avg('rating__rating')).order_by('-average_rating')
            elif order == 'countrating':
                if title:
                    movies = movies.values('id','title','genres').filter(title__icontains=title).annotate(view_cnt=Count('rating')).annotate(average_rating=Avg('rating__rating')).order_by('-view_cnt')
                elif genre:
                    movies = movies.values('id','title','genres').filter(genres__icontains=genre).annotate(view_cnt=Count('rating')).annotate(average_rating=Avg('rating__rating')).order_by('-view_cnt')
                else:
                    movies = movies.values('id', 'title', 'genres').annotate(view_cnt=Count('rating')).annotate(average_rating=Avg('rating__rating')).order_by('-view_cnt')
        else:
            if id:
                movies = movies.filter(pk=id)
            elif title:
                movies = movies.values('id','title',"genres").filter(title__icontains=title).annotate(view_cnt=Count('rating')).annotate(average_rating=Avg('rating__rating'))
            elif genre:
                movies = movies.values('id','title','genres').filter(genres__icontains=genre).annotate(view_cnt=Count('rating')).annotate(average_rating=Avg('rating__rating'))
            else:
                movies = movies.values('id', 'title', 'genres').annotate(view_cnt=Count('rating')).annotate(average_rating=Avg('rating__rating'))

        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        movie = Movie.objects.all()
        movie.delete()
        return Response(status=status.HTTP_200_OK)
    if request.method == 'UPDATE':
        id = request.GET.get('id', None)
        if id:
            Movie.objects.filter(pk=id).update()

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
def rank(request):
    if request.method == 'GET':
        order = request.GET.get('order')
        profile = Profile.objects.all()
        if order == 'age':
            rank = request.GET.get('rank')
            if rank == '10':
                profile = profile.values('id').filter(age__lt=18)
            elif rank == '20':
                profile = profile.values('id').filter(age__range=(19,28))
            elif rank == '30':
                profile = profile.values('id').filter(age__range=(29, 38))
            elif rank == '40':
                profile = profile.values('id').filter(age__range=(39, 48))
            elif rank == '50':
                profile = profile.values('id').filter(age__gt=49)
        elif order == 'gender':
            gender = request.GET.get('gender')
            profile = Profile.objects.all()
            if gender == 'M':
                profile = profile.values('id').filter(gender='M')
            elif gender == 'F':
                profile = profile.values('id').filter(gender='F')
        elif order == 'occupation':
            occupation = request.GET.get('occupation')
            profile = Profile.objects.all()
            profile = profile.values('id').filter(occupation__icontains=occupation)
        movies = Movie.objects.filter(rating__userid__in=profile).annotate(rate=Count('rating')).order_by('-rate')[:10]
        serializer = RankSerializer(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
