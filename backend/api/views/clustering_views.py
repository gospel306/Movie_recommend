import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn import preprocessing
from sklearn.mixture import GaussianMixture

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg, Count
from api.serializers import MovieSerializer
from api.models import MovieCluster, Movie, Profile, Rating

@api_view(['GET'])
def clustering(request):
    if request.method == 'GET':
        type = request.GET.get('type', None)
        data = request.GET.get('data', None)
        clusteringnum = int(request.GET.get('clusteringnum', None))
        if data == 'movie':
            movies = Movie.objects.all()
            movies = movies.values('id', 'title', 'genres')
            # movie data manufacturing
            manufacturedMovieData = open("movieParsing.dat", 'w')
            manufacturedMovieData.write("MovieID,Action,Adventure,Animation,Children's,Comedy,Crime,Documentary,Drama,Fantasy,Film-Noir,Horror,Musical,Mystery,Romance,Sci-Fi,Thriller,War,Western\n")
            
            genreAll = ["Action","Adventure","Animation","Children's","Comedy","Crime","Documentary","Drama","Fantasy","Film-Noir","Horror","Musical","Mystery","Romance","Sci-Fi","Thriller","War","Western"]

            for row in movies.values_list():
                inputStr = str(row[0])
                genreArr = row[2].split("|")

                idx = 0
                for genre in genreAll:
                    if idx < len(genreArr) and genre == genreArr[idx]:
                        inputStr += ",1"
                        idx += 1
                    else:
                        inputStr += ",0"

                inputStr += "\n"
                manufacturedMovieData.write(inputStr)
            manufacturedMovieData.close()

            df = pd.read_csv('movieParsing.dat')
            X = np.array(df.drop(['MovieID'], 1).astype(float))
            X = preprocessing.scale(X)
        elif data == 'user':
            # user data manufacturing
            profiles = Profile.objects.all()
            profiles = profiles.values('id','age','gender','occupation')

            manufacturedUserData = open("C:\\Users\\multicampus\\Desktop\\bigdataSub2\\bigdata-sub2\\backend\\userParsing.dat",'w')
            manufacturedUserData.write("UserID,age,gender,occupation,clusterNum\n")
            occupationAll = ["other","academic/educator","artist","clerical/admin","college/grad student","customer service","doctor/health care","executive/managerial","farmer","homemaker","K-12 student","lawyer","programmer","retired","sales/marketing","scientist","self-employed","technician/engineer","tradesman/craftsman","unemployed","writer"]
            
            for row in profiles.values_list():
                inputStr = str(row[1])+","+str(row[3])
                if(row[2]=='M'):
                    inputStr += ",1"
                else:
                    inputStr += ",2"

                for i in range(0,21):
                    if occupationAll[i] == row[4]:
                        inputStr += ","+str(i)

                # 영화정보 불러와서 추가해주기
                # 유저가 본 영화 중 클러스터링 맥스값 가져오기
                ratings = Rating.objects.all()
                ratings = ratings.filter(userid=row[1])
                ratings = ratings.values('movieid_id')
                
                max = 0
                for mid in ratings.values_list():
                    moviecluster = MovieCluster.objects.all()
                    moviecluster = moviecluster.filter(movieid=mid[2])
                    moviecluster = moviecluster.values('clusternum')

                    if len(moviecluster) <= 0:
                        pass
                    else:
                        mcs = moviecluster[0]["clusternum"]
                        if(max < mcs):
                            max = mcs

                inputStr += ","+str(max)+"\n"
                
                if row[1]==1 :
                    continue
                else :
                    print(inputStr)
                    manufacturedUserData.write(inputStr)
            manufacturedUserData.close()

            df = pd.read_csv('userParsing.dat')
            X = np.array(df.drop(['UserID'], 1).astype(float))
        if type == 'K-Means':
            clf = KMeans(n_clusters=clusteringnum)
            clf.fit(X)
            result = clf.labels_
        elif type == 'Hierarchical':
            clf = AgglomerativeClustering(n_clusters=clusteringnum)
            clf.fit(X)
            result = clf.labels_
        elif type == 'EM':
            clf = GaussianMixture(n_components=clusteringnum)
            result = clf.fit_predict(X)

        if data == 'movie':
            moviecluster = MovieCluster.objects.all()
            count = 1
            moviecluster.delete()
            print(result.size)
            for dat in result:
                try:
                    movieid = Movie.objects.get(pk=count)
                except :
                    count += 1
                    continue
                MovieCluster(movieid=movieid, clusternum=dat).save()
                count += 1

    return Response(data=True, status=status.HTTP_200_OK)


@api_view(['GET'])
def getsimilar(request):
    if request.method == 'GET':
        movieid = request.GET.get('movieid', None)
        if movieid:
            num = MovieCluster.objects.values('clusternum').get(movieid=movieid)
            moviecluster = MovieCluster.objects.values('movieid').filter(clusternum=num['clusternum'])
            movies = Movie.objects.all().values('id', 'title', 'genres').annotate(view_cnt=Count('rating')).annotate(average_rating=Avg('rating__rating'))
            movies = movies.filter(pk__in=moviecluster)
            print(movies)
            serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
