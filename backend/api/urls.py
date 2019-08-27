from django.conf.urls import url
from api.views import movie_views
from api.views import auth_views
from api.views import rating_views

urlpatterns = [
    url('auth/signup-many/$', auth_views.signup_many, name='sign_up_many'),
    url('movies/$', movie_views.movies, name='movie_list'),
    url('ratings/$', rating_views.ratings, name='rating_list'),
    url('rank/$', movie_views.rank, name='movie_list')
]
