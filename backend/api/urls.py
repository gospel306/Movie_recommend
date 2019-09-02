from django.conf.urls import url
from api.views import movie_views
from api.views import auth_views
from api.views import rating_views
from api.views import signUp_views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url('auth/signup-many/$', auth_views.signup_many, name='sign_up_many'),
    url('movies/$', movie_views.movies, name='movie_list'),
    url('ratings/$', rating_views.ratings, name='rating_list'),
    url('login/$', obtain_jwt_token),
    url('signup/$',signUp_views.signup, name='sign_up_user'),
]
