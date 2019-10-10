from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Rating, Table_KNN_user, Table_KNN_movie, Movie, Profile, MovieCluster
from api.serializers import RatingSerializer
from django.contrib.auth.models import User
import math
import numpy as np
from numpy import linalg as la
import random

def sim_pearson(data, name1, name2):
    avg_name1 = 0
    avg_name2 = 0
    count = 0
    for movies in data[name1]:
        if movies in data[name2]:
            avg_name1 += data[name1][movies]
            avg_name2 += data[name2][movies]
            count += 1

    if count == 0:
        return -1
    elif count == 1:
        return 0

    avg_name1 = avg_name1 / count
    avg_name2 = avg_name2 / count

    sum_name1 = 0
    sum_name2 = 0
    sum_name1_name2 = 0
    for movies in data[name1]:
        if movies in data[name2]:
            sum_name1 += pow(data[name1][movies] - avg_name1, 2)
            sum_name2 += pow(data[name2][movies] - avg_name2, 2)
            sum_name1_name2 += (data[name1][movies] - avg_name1) * (data[name2][movies] - avg_name2)

    tmp = (math.sqrt(sum_name1) * math.sqrt(sum_name2))

    if tmp == 0:
        return -1
    else:
        return sum_name1_name2 / tmp


def top_match(data, name, index=3, sim_function=sim_pearson):
    li = []
    for i in data:
        if name != i:
            li.append((sim_function(data, name, i), i))
    li.sort()
    li.reverse()
    return li[:index]


def getRecommendation(data, person, k=3, sim_function=sim_pearson):
    result = top_match(data, person, k)

    score = 0
    li = list()
    score_dic = dict()
    sim_dic = dict()

    for sim, name in result:
        if sim < 0: continue
        for movie in data[name]:
            if movie not in data[person]:
                score += sim * data[name][movie]
                score_dic.setdefault(movie, 0)
                score_dic[movie] += score

                sim_dic.setdefault(movie, 0)
                sim_dic[movie] += sim

            score = 0

    for key in score_dic:
        if sim_dic[key] == 0:
            continue
        score_dic[key] = score_dic[key] / sim_dic[key]
        li.append((score_dic[key], key))
    li.sort()
    li.reverse()
    return li


@api_view(['GET'])
def knnAlgorithm(request):
    if request.method == 'GET':
        userid = request.GET.get('user_id', None)
        movieid = request.GET.get('movie_id', None)
        exe = request.GET.get('exe', None)

        ratings = Rating.objects.all()

        if exe:
            ##### 유저 KNN #####
            userDict1 = dict()
            for i in range(2, 6043):
                eachUserRatings = ratings.filter(userid=i)
                eachUserRatings = eachUserRatings.order_by('movieid_id')

                movieDict1 = dict()

                for rate in eachUserRatings:
                    movieDict1[rate.movieid_id] = rate.rating

                userDict1[i] = movieDict1

            tableKNNUser = Table_KNN_user.objects.all()
            tableKNNUser.delete()
            for i in range(2, 6043):
                movieRank = getRecommendation(userDict1, i)[:10]
                Table_KNN_user(user_id=i, movie=movieRank).save()

            ##### 영화 KNN #####
            tableKNNMoive = Table_KNN_movie.objects.all()
            tableKNNMoive.delete()
            
            recommend_movie_list = []
            moviecluster = MovieCluster.objects.all()
            for movieidx in range(1, 3952):
                clusterNum = moviecluster.filter(movieid=movieidx)
                clusterNum = clusterNum.values('clusternum')
                if clusterNum:
                    clusterNum = clusterNum[0]['clusternum']
                    clusterMovies = moviecluster.filter(clusternum=clusterNum)
                    clusterMovies = clusterMovies.values('movieid')

                    inputUserList = []
                    for i in range(10):
                        inputUserList.append(random.choice(clusterMovies)['movieid'])
                    Table_KNN_movie(movie_id=movieidx, user=inputUserList).save()
                else :
                    continue

            return Response(status=status.HTTP_200_OK)

        result = []

        if userid:
            id = User.objects.get(username=userid)
            users = Table_KNN_user.objects.all()
            users = users.filter(user=id.id)
            result = users.values('movie', 'user_id')

        if movieid:
            users = Table_KNN_movie.objects.all()
            users = users.filter(movie=movieid)
            result = users.values('user', 'movie_id')

        return Response(data=result, status=status.HTTP_200_OK)
