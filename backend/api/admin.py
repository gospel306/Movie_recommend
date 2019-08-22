from django.contrib import admin
from .models import Profile,Movie, Rating

admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Rating)