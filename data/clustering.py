import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn import preprocessing
from matplotlib import colors as mcolors
import math

df = pd.read_csv('movieParsing.dat')
X = np.array(df.drop(['MovieID'], 1).astype(float))
X = preprocessing.scale(X)

clf = KMeans(n_clusters=10)
clf.fit(X)
print(clf.labels_)
print(clf.labels_[0])



