from .models import Profile, Movie, Rating
from rest_framework import serializers
from django.db.models import Avg,Count

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
        return obj.rating

class MovieSerializer(serializers.ModelSerializer):
   genres_array = serializers.ReadOnlyField()
   view_cnt = serializers.SerializerMethodField('get_view_cnt')
   average_rating = serializers.SerializerMethodField('get_average_rating')
   class Meta:
       model = Movie
       fields = ('id', 'title', 'genres_array','view_cnt','average_rating','genres')
   def get_view_cnt(self, obj):
       return obj['view_cnt']
   def get_average_rating(self, obj):
       print(obj)
       return obj['average_rating']



class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('userid', 'movieid', 'rating', 'timestamp')
