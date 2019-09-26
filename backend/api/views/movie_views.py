from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie, Rating, Profile, Person
from api.serializers import MovieSerializer
from rest_framework.response import Response
from django.db.models import Avg, Count
from imdb import IMDb
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup


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
        movies = movies.values('id', 'title', 'genres')
        ia = IMDb()
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
        for movie in movies:
            print(movie['title'])
            imovie = ia.search_movie(movie['title'])
            mid = imovie[0].getID()
            imovie = ia.get_movie(mid)
            m = Movie.objects.get(pk=movie['id'])
            print(imovie.keys())
            if m.poster == '' and 'full-size cover url' in imovie.keys():
                Movie.objects.filter(pk=movie['id']).update(poster=imovie['full-size cover url'])
            if m.video == '':
                req = requests.get('https://www.imdb.com/title/tt'+mid)
                html = req.text
                soup = BeautifulSoup(html, 'lxml')
                titles = soup.select('#title-overview-widget > div.vital > div.slate_wrapper > div.slate > a')
                link = 'https://www.imdb.com'
                for title in titles:
                    link = link + title.get('href')
                Movie.objects.filter(pk=movie['id']).update(video=link)
            if m.plot == '' and 'plot' in imovie.keys():
                Movie.objects.filter(pk=movie['id']).update(plot=imovie['plot'])
            for cast in imovie['cast']:
                people = Person.objects.filter(pk=cast.personID)
                if not people:
                    person = ia.get_person(cast.personID)
                    name = None
                    height = None
                    spouse = None
                    biography = None
                    birth_date = None
                    birth_notes = None
                    headshot = None
                    if 'name' in person.keys():
                        name = person['name']
                    if 'spouse' in person.keys():
                        spouse = '|'.join(person['spouse'])
                    if 'height' in person.keys():
                        height = person['height']
                    if 'mini biography' in person.keys():
                        biography = person['mini biography']
                    if 'birth date' in person.keys():
                        try:
                            birth_date = datetime.strptime(person['birth date'], "%Y-%m-%d") + timedelta(hours=10)
                        except:
                            print("error")
                    if 'birth notes' in person.keys():
                        birth_notes = person['birth notes']
                    if 'full-size headshot' in person.keys():
                        headshot = person['full-size headshot']

                    Person(id=cast.personID, name=name, height=height, spouse=spouse, biography=biography,
                           birth_date=birth_date, birch_notes=birth_notes, headshot=headshot).save()
                m = Movie.objects.get(pk=movie['id'])
                p = Person.objects.get(pk=cast.personID)
                m.cast.add(p)
            for director in imovie['director']:
                people = Person.objects.filter(pk=director.personID)
                if not people:
                    person = ia.get_person(cast.personID)
                    name = None
                    height = None
                    spouse = None
                    biography = None
                    birth_date = None
                    birth_notes = None
                    headshot = None
                    if 'name' in person.keys():
                        name = person['name']
                    if 'spouse' in person.keys():
                        spouse = '|'.join(person['spouse'])
                    if 'height' in person.keys():
                        height = person['height']
                    if 'mini biography' in person.keys():
                        biography = person['mini biography']
                    if 'birth date' in person.keys():
                        try:
                            birth_date = datetime.strptime(person['birth date'], "%Y-%m-%d") + timedelta(hours=10)
                        except:
                            print("error")
                    if 'birth notes' in person.keys():
                        birth_notes = person['birth notes']
                    if 'full-size headshot' in person.keys():
                        headshot = person['full-size headshot']

                    Person(id=cast.personID, name=name, height=height, spouse=spouse, biography=biography,
                           birth_date=birth_date, birch_notes=birth_notes, headshot=headshot).save()
                m = Movie.objects.get(pk=movie['id'])
                p = Person.objects.get(pk=cast.personID)
                m.director.add(p)

            for writer in imovie['writer']:
                people = Person.objects.filter(pk=writer.personID)
                if not people:
                    person = ia.get_person(cast.personID)
                    name = None
                    height = None
                    spouse = None
                    biography = None
                    birth_date = None
                    birth_notes = None
                    headshot = None
                    if 'name' in person.keys():
                        name = person['name']
                    if 'spouse' in person.keys():
                        spouse = '|'.join(person['spouse'])
                    if 'height' in person.keys():
                        height = person['height']
                    if 'mini biography' in person.keys():
                        biography = person['mini biography']
                    if 'birth date' in person.keys():
                        try:
                            birth_date = datetime.strptime(person['birth date'], "%Y-%m-%d") + timedelta(hours=10)
                        except:
                            print("error")
                    if 'birth notes' in person.keys():
                        birth_notes = person['birth notes']
                    if 'full-size headshot' in person.keys():
                        headshot = person['full-size headshot']

                    Person(id=cast.personID, name=name, height=height, spouse=spouse, biography=biography, birth_date=birth_date, birch_notes=birth_notes, headshot=headshot).save()
                m = Movie.objects.get(pk=movie['id'])
                p = Person.objects.get(pk=cast.personID)
                m.writer.add(p)

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
        print(movies)
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
