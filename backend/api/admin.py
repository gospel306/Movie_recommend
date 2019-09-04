from django.contrib import admin
from .models import Profile,Movie, Rating, MovieCluster

admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(MovieCluster)