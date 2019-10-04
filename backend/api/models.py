from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, default='M')
    age = models.IntegerField(default=25)
    occupation = models.CharField(max_length=200)


#  wrapper for create user Profile
def create_profile(**kwargs):

    user = User.objects.create_user(
        username=kwargs['username'],
        password=kwargs['password'],
        is_active=True,
    )

    profile = Profile.objects.create(
        user=user,
        gender=kwargs['gender'],
        age=kwargs['age'],
        occupation=kwargs['occupation']
    )

    return profile


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=500)

    @property
    def genres_array(self):
        return self.genres.strip().split('|')


class Rating(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    movieid = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    timestamp = models.IntegerField()


class MovieCluster(models.Model):
    movieid = models.ForeignKey(Movie, on_delete=models.CASCADE)
    clusternum = models.IntegerField()


class UserCluster(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    clusternum = models.IntegerField()


class Table_MF(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.CharField(max_length=10, default='0')


class Table_KNN_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.TextField()


class Table_KNN_movie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.TextField()