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

@api_view(['GET'])
def update(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        ia = IMDb()
        for movie in movies:
            print(movie.title)
            if movie.id < 32:
                continue
            try:
                imovie = ia.search_movie(movie.title)
            except :
                continue
            mid = imovie[0].getID()
            imovie = ia.get_movie(mid)
            m = Movie.objects.get(pk=movie.id)

            if m.poster == '' and 'full-size cover url' in imovie.keys():
                Movie.objects.filter(pk=movie.id).update(poster=imovie['full-size cover url'])
            if m.video == '':
                req = requests.get('https://www.imdb.com/title/tt'+mid)
                html = req.text
                soup = BeautifulSoup(html, 'lxml')
                titles = soup.select('#title-overview-widget > div.vital > div.slate_wrapper > div.slate > a')
                link = ''
                for title in titles:
                    link = 'https://www.imdb.com' + title.get('href')
                Movie.objects.filter(pk=movie.id).update(video=link)
            if m.plot == '' and 'plot' in imovie.keys():
                Movie.objects.filter(pk=movie.id).update(plot=imovie['plot'])

            for cast in imovie['cast']:
                people = Person.objects.filter(pk=cast.personID)
                if not people:
                    person = ia.get_person(cast.personID)
                    print(cast.personID)
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
                m = Movie.objects.get(pk=movie.id)
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
                m = Movie.objects.get(pk=movie.id)
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
                m = Movie.objects.get(pk=movie.id)
                p = Person.objects.get(pk=cast.personID)
                m.writer.add(p)
