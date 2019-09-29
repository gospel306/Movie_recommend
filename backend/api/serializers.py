from .models import Profile, Movie, Rating, SubScribe, Person
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.SerializerMethodField('get_username')
    is_staff = serializers.SerializerMethodField('get_is_staff')
    rating = serializers.SerializerMethodField('get_rating')

    class Meta:
        model = Profile
        fields = ('id', 'username', 'is_staff', 'gender', 'age', 'occupation','rating')

    def get_username(self, obj):
        return obj.user.username

    def get_is_staff(self, obj):
        return obj.user.is_staff
    
    def get_rating(self, obj):
        if hasattr(obj, 'rating') is True:
            a = obj.rating
        else:
            a = ''
        return a


class MovieSerializer(serializers.ModelSerializer):
   genres_array = serializers.ReadOnlyField()
   view_cnt = serializers.SerializerMethodField('get_view_cnt')
   average_rating = serializers.SerializerMethodField('get_average_rating')

   class Meta:
       model = Movie
       fields = ('id', 'title', 'genres_array', 'view_cnt', 'average_rating', 'genres')

   def get_view_cnt(self, obj):
       if 'view_cnt' in obj.keys():
           num = obj['view_cnt']
       else:
           num = ''
       return num

   def get_average_rating(self, obj):
       if 'average_rating' in obj.keys():
           num = obj['average_rating']
       else:
           num = ''
       return num


class UserMovieSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField('get_rating')

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genres', 'rating')

    def get_rating(self,obj):
        rating = obj.rating
        return rating


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('userid', 'movieid', 'rating', 'timestamp')


class SubScribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubScribe
        fields = ('userid', 'startdate', 'subscribedate', 'autoscribe')


class MovieDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genres', 'writer', 'director', 'cast', 'poster', 'video', 'plot')


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('id', 'name', 'height', 'spouse', 'biography', 'birth_date', 'birch_notes', 'headshot')


class UserRatingSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField('get_title')
    genres = serializers.SerializerMethodField('get_genres')

    class Meta:
        model = Rating
        fields = ('userid', 'movieid', 'rating', 'timestamp', 'title','genres',)

    def get_title(self,obj):
        title = obj.movieid.title
        return title
    
    def get_genres(self,obj):
        genres = obj.movieid.genres
        return genres

