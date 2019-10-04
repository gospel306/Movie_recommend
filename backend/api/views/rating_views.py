from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Rating, Movie, User, Profile
from api.serializers import RatingSerializer, UserMovieSerializer, UserRatingSerializer
from django.db.models import F


@api_view(['GET', 'POST', 'DELETE'])
def ratings(request):

    if request.method == 'GET':
        userid = request.GET.get('userid', request.GET.get('userid',None))
        movieid = request.GET.get('movieid', request.GET.get('movieid', None))
        rating = request.GET.get('rating', None)
        timestamp = request.GET.get('timestamp', None)
        username = request.GET.get('username',None)
        ratings = Rating.objects.all()

        if userid:
            ratings = ratings.filter(userid=userid)
        if movieid:
            ratings = ratings.filter(movieid=movieid)
        if rating:
            ratings = ratings.filter(rating=rating)
        if timestamp:
            ratings = ratings.filter(timestamp=timestamp)
        if username:
            user = User.objects.get(username=username)
            if user:
                ratings = Rating.objects.filter(userid=user.id)
                ratings = ratings.select_related('movieid')                

        serializer = UserRatingSerializer(ratings, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        rating = Rating.objects.all()
        rating.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'POST':
        ratings = request.data.get('ratings', None)

        if ratings :
            for ratingg in ratings:
                userid = int(ratingg.get('userid', None))
                movieid = int(ratingg.get('movieid', None))
                rating = ratingg.get('rating', None)
                timestamp = ratingg.get('timestamp', None)
                userid = User.objects.get(pk=userid+1)
                movieid = Movie.objects.get(pk=movieid)

                if not (userid and movieid and rating and timestamp):
                    continue
                Rating(userid=userid, movieid=movieid, rating=rating, timestamp=timestamp).save()
        else :
            userid = User.objects.get(username=request.data.get('userid',None))
            movieid = request.data.get('movieid',None)
            rating = request.data.get('rating',None)
            timestamp = request.data.get('timestamp',None)
            movieid = Movie.objects.get(pk=movieid)
            check = Rating.objects.filter(userid = userid).filter(movieid=movieid)
            
            if userid and movieid and rating and timestamp :
                if not check :
                    Rating(userid = userid, movieid = movieid, rating = rating, timestamp = timestamp).save()
                else :
                    Rating.objects.filter(userid=userid,movieid=movieid).update(rating=rating,timestamp=timestamp)

        return Response(status=status.HTTP_200_OK)