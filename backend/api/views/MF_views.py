from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Rating, Table_MF, Movie
from api.serializers import RatingSerializer

import numpy as np

def my_round(n, decimals=0):
    expoN = n * 10 ** decimals
    if abs(expoN) - abs(np.floor(expoN)) < 0.5:
        return np.floor(expoN) / 10 ** decimals
    return np.ceil(expoN) / 10 ** decimals

class MatrixFactorization():
    def __init__(self, R, k, learning_rate, reg_param, epochs, verbose=False):
        self._R = R
        self._num_users, self._num_items = R.shape
        self._k = k
        self._learning_rate = learning_rate
        self._reg_param = reg_param
        self._epochs = epochs
        self._verbose = verbose


    def fit(self):
        self._P = np.random.normal(size=(self._num_users, self._k))
        self._Q = np.random.normal(size=(self._num_items, self._k))

        self._b_P = np.zeros(self._num_users)
        self._b_Q = np.zeros(self._num_items)
        self._b = np.mean(self._R[np.where(self._R != 0)])

        self._training_process = []
        for epoch in range(self._epochs):

            for i in range(self._num_users):
                for j in range(self._num_items):
                    if self._R[i, j] > 0:
                        self.gradient_descent(i, j, self._R[i, j])
            cost = self.cost()
            self._training_process.append((epoch, cost))

            # if self._verbose == True and ((epoch + 1) % 10 == 0):
            print("Iteration: %d ; cost = %.4f" % (epoch + 1, cost))

    def cost(self):
        xi, yi = self._R.nonzero()
        predicted = self.get_complete_matrix()
        cost = 0
        for x, y in zip(xi, yi):
            cost += pow(self._R[x, y] - predicted[x, y], 2)
        return np.sqrt(cost) / len(xi)

    def gradient(self, error, i, j):
        dp = (error * self._Q[j, :]) - (self._reg_param * self._P[i, :])
        dq = (error * self._P[i, :]) - (self._reg_param * self._Q[j, :])
        return dp, dq

    def gradient_descent(self, i, j, rating):
        prediction = self.get_prediction(i, j)
        error = rating - prediction

        self._b_P[i] += self._learning_rate * (error - self._reg_param * self._b_P[i])
        self._b_Q[j] += self._learning_rate * (error - self._reg_param * self._b_Q[j])

        dp, dq = self.gradient(error, i, j)
        self._P[i, :] += self._learning_rate * dp
        self._Q[j, :] += self._learning_rate * dq

    def get_prediction(self, i, j):
        return self._b + self._b_P[i] + self._b_Q[j] + self._P[i, :].dot(self._Q[j, :].T)

    def get_complete_matrix(self):
        return self._b + self._b_P[:, np.newaxis] + self._b_Q[np.newaxis:, ] + self._P.dot(self._Q.T)


@api_view(['GET'])
def mfAlgorithm(request):
    if request.method == 'GET':
        userid = request.GET.get('user_id', None)
        exe = request.GET.get('exe',None)

        ratings = Rating.objects.all()
        if exe:
            ratings = ratings.values('movieid_id','userid_id','rating')
            tmp = np.zeros((6043,3953))
            for r in ratings:
                tmp[r['userid_id']][ r['movieid_id']] = r['rating']

            R = np.zeros((6041,3952))
            for i in range(2,len(tmp)):
                R[i-2] = tmp[i][1:]

            factorizer = MatrixFactorization(R, k=3, learning_rate=0.01, reg_param=0.01, epochs=3, verbose=True)
            factorizer.fit()
            
            D = factorizer.get_complete_matrix()

            # print(D)
            movies = Movie.objects.all()
            movies = movies.values('id')
            
            tableMF = Table_MF.objects.all()
            tableMF.delete()
            for i in range(2,len(D)):
              for m in movies:
                  Table_MF(movie_id=m['id'], user_id=i, rating=my_round(D[i-2][m['id']-1],1)).save()
            return Response(status=status.HTTP_200_OK)
        
        if userid:
            movies = Table_MF.objects.all()
            movies = movies.filter(user=userid)
            movies = movies.values('rating','movie_id').order_by('-rating')

            ratings = ratings.filter(userid=userid)
            ratings = ratings.values('movieid')

            result = []

            for i in range(10):
                idx = 100+(10*i)
                for movie in ratings:
                    if movie['movieid']==movies[idx]['movie_id']:
                        idx = idx + 1
                        break
                result.append(movies[idx])
            return Response(data=result, status=status.HTTP_200_OK)
