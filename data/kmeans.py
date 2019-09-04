import pandas as pd
import numpy as np
from sklearn import preprocessing

class K_Means:
    def __init__(self, k, input):
        self.k = k
        self.df = input
        self.C = None

    def centroids(self):
        import random
        C = {i:[data for data in self.df.values[i]] for i, j in zip(range(self.k), random.sample(range(len(self.df)), self.k))}
        return C

    def classify(self, C):
        import copy
        cluster_df = copy.deepcopy(self.df)
        col_n=cluster_df.shape[1]
        for i in C.keys():
            cluster_df["Distance_from_{}".format(i)]=np.linalg.norm(np.array(cluster_df)[:, :col_n]-C[i], axis=1)
        dist_cols=["Distance_from_{}".format(i) for i in C.keys()]
        cluster_df["Closet_Cluster"]=cluster_df.loc[:, dist_cols].idxmin(axis=1).map(lambda x: int(x.lstrip("Distance_from_")))
        return cluster_df

    def update(self, C):
        c_df = self.classify(C)
        self.C = {
            i:[c for c in np.mean(self.df[c_df["Closet_Cluster"]==i], axis=0)] for i in c_df["Closet_Cluster"].unique()
        }
        return self.C

    def train_cluster(self):
        assignments = None
        C = self.centroids()
        while True:
            cluster_df = self.classify(C)
            new_assignments = list(self.classify(C)["Closet_Cluster"])
            new_C = self.update(C)
            if assignments == new_assignments:
                break
            assignments = new_assignments
            C = new_C
        return new_C, np.array(new_assignments), cluster_df


df = pd.read_csv('movieParsing.dat')
X = np.array(df.drop(['MovieID'], 1).astype(float))
X = preprocessing.scale(X)
Y = np.array(df['MovieID'])

model1 = K_Means(3, X)

print(model1.train_cluster())

print(model1.train_cluster()[2])