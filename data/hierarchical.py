import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn import preprocessing
from sklearn.mixture import GaussianMixture

np.set_printoptions(precision=4, suppress=True)
plt.figure(figsize=(10, 3))

df = pd.read_csv('movieParsing.dat')
X = np.array(df.drop(['MovieID'], 1).astype(float))
X = preprocessing.scale(X)
clf = AgglomerativeClustering(n_clusters=10)
clf.fit(X)
print(clf.labels_)

clf2 = GaussianMixture(n_components=10)
a = clf2.fit_predict(X)
print(a)

clf3 = KMeans(n_clusters=10)
clf3.fit(X)
print(clf3.labels_)

