from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Rating, Movie, User, Profile
from api.serializers import RatingSerializer


@api_view(['GET', 'POST', 'DELETE'])
def ratings(request):

    if request.method == 'GET':
        userid = request.GET.get('userid', request.GET.get('userid',None))
        movieid = request.GET.get('movieid', request.GET.get('movieid', None))
        rating = request.GET.get('rating', None)
        timestamp = request.GET.get('timestamp', None)
        ratings = Rating.objects.all()

        if userid:
            ratings = ratings.filter(userid=userid)
        if movieid:
            ratings = ratings.filter(movieid=movieid)
        if rating:
            ratings = ratings.filter(rating=rating)
        if timestamp:
            ratings = ratings.filter(timestamp=timestamp)

        serializer = RatingSerializer(ratings, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        rating = Rating.objects.all()
        rating.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'POST':
        ratings = request.data.get('ratings', None)
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
        return Response(status=status.HTTP_200_OK)