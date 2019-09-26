from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import create_profile, Rating, Profile, Movie, SubScribe
from api.serializers import ProfileSerializer, MovieSerializer, UserMovieSerializer, SubScribeSerializer
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from pytz import timezone



@api_view(['POST', 'GET'])
def signup_many(request):

    if request.method == 'POST':
        profiles = request.data.get('profiles', None)
        for profile in profiles:
            username = profile.get('username', None)
            password = profile.get('password', None)
            age = profile.get('age', None)
            occupation = profile.get('occupation', None)
            gender = profile.get('gender', None)

            create_profile(username=username, password=password, age=age,
                           occupation=occupation, gender=gender)

        return Response(status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        movieid = request.GET.get('movieid', None)
        userid = request.GET.get('userid', None)
        if movieid:
            profiles = Profile.objects.raw('select api_profile.id, api_profile.user_id,api_profile.gender,api_profile.age,api_profile.occupation,api_rating.rating from api_movie,api_rating,api_profile where api_movie.id = api_rating.movieid_id and api_rating.userid_id = api_profile.user_id and api_movie.id = '+movieid)
            serializer = ProfileSerializer(profiles, many=True)
        elif userid:
            movies = Movie.objects.raw('select api_movie.id, api_movie.title,api_movie.genres, api_rating.rating as rating from api_profile,api_rating,api_movie where api_profile.user_id = api_rating.userid_id and api_movie.id = api_rating.movieid_id and api_profile.user_id = '+userid+' group by api_movie.id')
            serializer = UserMovieSerializer(movies, many=True)
        else:
            profiles = Profile.objects.all()
            serializer = ProfileSerializer(profiles, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['POST','PUT','DELETE'])
def users(request):

    if request.method == 'POST':
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        age = request.data.get('age', None)
        occupation = request.data.get('occupation', None)
        gender = request.data.get('gender', None)

        if username and password :
            create_profile(username=username, password=password, age=age,
                           occupation=occupation, gender=gender)

        return Response(status=status.HTTP_201_CREATED)

    if request.method == 'PUT':
        id = request.GET.get('id', None)
        age = request.GET.get('age', None)
        occupation = request.GET.get('occupation', None)
        if id and age and occupation:
            user = User.objects.get(pk=id)
            Profile.objects.filter(user=user).update(age=age, occupation=occupation)
        return Response(status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        id = request.GET.get('id',None)
        if id:
            user = User.objects.get(pk=id)
            if user:
                user.delete()

        return Response(status=status.HTTP_201_CREATED)


@api_view(['PUT', 'GET'])
def subscribe(request):
    koreadate = timezone('Asia/Seoul')
    if request.method == 'PUT':
        id = request.GET.get('id', None)
        if id:
            user = User.objects.get(pk=id)
            subscribe = SubScribe.objects.filter(userid=user)
            autoscribe = request.GET.get('auto')
            date = datetime.now(koreadate)
            if not subscribe:
                SubScribe(userid=user, startdate=date, subscribedate=date, autoscribe=autoscribe).save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                scribedate = subscribe.order_by("subscribedate")[0]
                scribekor = datetime.astimezone(scribedate.subscribedate, koreadate)
                if scribekor + timedelta(days=30) > date > scribekor:
                    SubScribe.objects.filter(pk=scribedate.id).update(subscribedate=scribekor+timedelta(days=30), autoscribe=autoscribe)
                else:
                    SubScribe(userid=user, startdate=date, subscribedate=date, autoscribe=autoscribe).save()
                return Response(status=status.HTTP_200_OK)
    if request.method == 'GET':
        id = request.GET.get('id', None)
        user = User.objects.get(pk=id)
        option = request.GET.get('option')
        date = request.GET.get('firstdate')
        firstdate = datetime.strptime(date, "%Y-%m-%d %H:%M")
        date = request.GET.get('lastdate')
        lastdate = datetime.strptime(date, "%Y-%m-%d %H:%M", None)
        scribedate = SubScribe.objects.filter(userid=user)
        if option == "list":
            scribedate = scribedate.filter(startdate__range=(firstdate, lastdate))
        elif option == "isscribe":
            scribedate = scribedate.filter(subscribedate__range=(firstdate, lastdate))
        elif option == "isauto":
            scribedate = scribedate.order_by("subscribedate")[0]
            if scribedate and scribedate.autoscribe:
                date = datetime.now(koreadate)
                SubScribe.objects.filter(pk=scribedate.id).update(subscribedate=date)
        scribedate = scribedate.order_by("subscribedate")
        serializer = SubScribeSerializer(scribedate, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)