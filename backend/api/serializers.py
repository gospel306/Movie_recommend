from .models import Profile, Movie, Rating, SubScribe, Person, Directors, Writers, Casts
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
       fields = ('id', 'title', 'genres_array', 'poster', 'view_cnt', 'average_rating', 'genres')

   def get_view_cnt(self, obj):
       return obj.view_cnt

   def get_average_rating(self, obj):
       return obj.average_rating


class UserMovieSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField('get_rating')

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genres', 'rating')

    def get_rating(self, obj):
        rating = obj.rating
        return rating


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('userid', 'movieid', 'rating', 'timestamp')


class SubScribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubScribe
        fields = ('userid', 'startdate', 'subscribedate', 'autoscribe', 'cluster')


class MovieDetailSerializer(serializers.ModelSerializer):
    writerlist = serializers.SerializerMethodField('get_writerlist')
    directorlist = serializers.SerializerMethodField('get_directorlist')
    castlist = serializers.SerializerMethodField('get_castlist')

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genres', 'writerlist', 'directorlist', 'castlist', 'poster', 'video', 'plot')

    def get_writerlist(self, obj):
        writerlist = []
        writers = Writers.objects.filter(movieid=obj.id)
        for writer in writers:
            writerlist.append(str(writer.personid_id) + ": " + Person.objects.get(id=writer.personid_id).name)
        return writerlist

    def get_directorlist(self, obj):
        directorlist = []
        directors = Directors.objects.filter(movieid=obj.id)
        for director in directors:
            directorlist.append(str(director.personid_id) + ": " + Person.objects.get(id=director.personid_id).name)
        return directorlist

    def get_castlist(self, obj):
        castlist = []
        casts = Casts.objects.filter(movieid=obj.id)
        for cast in casts:
            castlist.append(str(cast.personid_id) + ": " + Person.objects.get(id=cast.personid_id).name)
        return castlist


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('id', 'name', 'height', 'spouse', 'biography', 'birth_date', 'birch_notes', 'headshot')


class UserRatingSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField('get_title')
    genres = serializers.SerializerMethodField('get_genres')

    class Meta:
        model = Rating
        fields = ('userid', 'movieid', 'rating', 'timestamp', 'title', 'genres',)

    def get_title(self, obj):
        title = obj.movieid.title
        return title
    
    def get_genres(self, obj):
        genres = obj.movieid.genres
        return genres

