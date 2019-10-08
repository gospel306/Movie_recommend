from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie, Rating, Profile, Person
from rest_framework.response import Response
from imdb import IMDb
from datetime import datetime, timedelta
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY1 = "AIzaSyBUKiqE4FOE9bJZ7HCoh715DDz3SytoGGg"
DEVELOPER_KEY2 = "AIzaSyAt6i9G_OmPMASU3VqRVYyMYhhqlxn3V5s"
DEVELOPER_KEY3 = "AIzaSyAiFgPB8Qdi_VQ_ZSWwYgdgWM3A8rg8DCE"
DEVELOPER_KEY4 = "AIzaSyDPITG2gLYni_kAn4BZjnDfOh1-olhtVzA"
DEVELOPER_KEY5 = "AIzaSyBQZVbyEzMHGGOxhgq4v0Gz7Sp5t1Wy8KQ"
DEVELOPER_KEY6 = "AIzaSyBZUjPgA_m3adkk-7YGgomuqHCEuNjHuzw"
DEVELOPER_KEY7 = "AIzaSyCEWiR5RUpfyHZzjnqWozyINuzEypAroRc"

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(title, id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY1)

    search_response = youtube.search().list(
        q=title+" trailer",
        part="id",
        maxResults=1
    ).execute()

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            Movie.objects.filter(pk=id).update(video=search_result["id"]["videoId"])


@api_view(['GET'])
def update(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        ia = IMDb()
        for movie in movies:
            print(movie.title)
            if movie.id < 3458:
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
            # try:
            #     youtube_search(movie.title, movie.id)
            # except HttpError:
            #     print("An HTTP error %d occurred:\n%s")
            #     return
            if m.plot == '' and 'plot' in imovie.keys():
                Movie.objects.filter(pk=movie.id).update(plot=imovie['plot'])
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
                m = Movie.objects.get(pk=movie.id)
                p = Person.objects.get(pk=cast.personID)
                m.cast.add(p)
                # print(cast)
            for director in imovie['director']:
                people = Person.objects.filter(pk=director.personID)
                if not people:
                    person = ia.get_person(director.personID)
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

                    Person(id=director.personID, name=name, height=height, spouse=spouse, biography=biography,
                           birth_date=birth_date, birch_notes=birth_notes, headshot=headshot).save()
                m = Movie.objects.get(pk=movie.id)
                p = Person.objects.get(pk=director.personID)
                m.director.add(p)
                # print(director)
            for writer in imovie['writers']:
                if writer.personID is None:
                    continue
                people = Person.objects.filter(pk=writer.personID)
                if not people:
                    person = ia.get_person(writer.personID)
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

                    Person(id=writer.personID, name=name, height=height, spouse=spouse, biography=biography, birth_date=birth_date, birch_notes=birth_notes, headshot=headshot).save()
                m = Movie.objects.get(pk=movie.id)
                p = Person.objects.get(pk=writer.personID)
                m.writer.add(p)
                # print(writer)

