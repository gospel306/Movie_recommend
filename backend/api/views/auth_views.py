from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import create_profile, Rating, Profile, Movie
from api.serializers import ProfileSerializer,MovieSerializer


@api_view(['POST','GET'])
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
            movies = Movie.objects.raw('select api_movie.id, api_movie.title,api_movie.genres, count(api_rating.rating) as view_cnt from api_profile,api_rating,api_movie where api_profile.user_id = api_rating.userid_id and api_profile.user_id = '+userid+' group by api_movie.id')
            serializer = MovieSerializer(movies, many=True)
        else:
            profiles = Profile.objects.all()
            serializer = ProfileSerializer(profiles, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)