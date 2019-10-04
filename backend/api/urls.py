from django.conf.urls import url
from api.views import movie_views, auth_views, rating_views, clustering_views, person_view, KNN_views, update_view, MF_views
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
    url('update/$', update_view.update, name='update'),
    url('moviedetail/$', movie_views.moviedetail, name='moviedetail'),
    url('person/$', person_view.person, name='person'),
    url('KNN/$', KNN_views.knnAlgorithm, name='KNN'),
    url('MF/', MF_views.mfAlgorithm, name='MF')
]
