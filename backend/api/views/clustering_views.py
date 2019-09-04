import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn import preprocessing
from sklearn.mixture import GaussianMixture

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import MovieCluster, Movie

@api_view(['GET'])
def clustering(request):
    if request.method == 'GET':
        type = request.GET.get('type', None)
        data = request.GET.get('data', None)
        clusteringnum = request.GET.get('clusteringnum', None)
        if data == 'movie':
            movies = Movie.objects.all()
            movies = movies.values('id', 'title', 'genres')
            # movie data manufacturing
            manufacturedMovieData = open("C:\\Users\\multicampus\\Desktop\\bigdataSub2\\bigdata-sub2\\backend\\api\\movieParsing.dat",'w')
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
            for dat in result:
                obj, created = moviecluster.get_or_create(
                    movieid=count,
                    clusternum=dat
                )
                if created == False:
                    moviecluster.filter(pk=count).update(clusternum=dat)
                count += 1

    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def getsimilar(request):
    if request.method == 'GET':
        movieid = request.GET.get('movieid',None)
        if movieid:
            moviecluster = MovieCluster.objects.filter(movieid=movieid)
            movie = Movie.objects.filter(pk__in=moviecluster)