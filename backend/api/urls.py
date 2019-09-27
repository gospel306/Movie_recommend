from django.conf.urls import url
from api.views import movie_views
from api.views import auth_views
from api.views import rating_views
from api.views import clustering_views
from api.views import KNN_views, update_view
from api.views import MF_views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url('auth/signup-many/$', auth_views.signup_many, name='sign_up_many'),
    url('movies/$', movie_views.movies, name='movie_list'),
    url('ratings/$', rating_views.ratings, name='rating_list'),
    url('login/$', obtain_jwt_token),
    url('users/$',auth_views.users, name='users'),
    url('cluster/$', clustering_views.clustering, name='cluster'),
    url('similar/$', clustering_views.getsimilar, name='getsimilar'),
    url('subscribe/$', auth_views.subscribe, name='subscribe'),
    url('KNN/$', KNN_views.communication, name='KNN'),
    url('update/$', update_view.update, name='update')
    # url('MF/', MF_views.communication, name='MF')
]
