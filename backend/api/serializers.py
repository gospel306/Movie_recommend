from .models import Profile, Movie, Rating
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
       fields = ('id', 'title', 'genres_array','view_cnt','average_rating','genres')

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


class RankSerializer(serializers.ModelSerializer):
    genres_array = serializers.ReadOnlyField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genres_array', 'genres')


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('userid', 'movieid', 'rating', 'timestamp')
