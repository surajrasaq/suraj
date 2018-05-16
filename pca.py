# Author Surajudeen Abdulrasaq

# University of Lyon/University Jean Monnet France

"""
==========================================
PCA
==========================================

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import csv

activity = pd.read_csv('./datas/novins_final',  delimiter = ',')

#activity1 = pd.read_csv('./datas/new_novins.csv',  delimiter = ',')

#pd.to_datetime(activity['date'])
activity.dropna(inplace= True)
del activity['date']
# del activity['activity_end']

x = StandardScaler().fit_transform(activity)

#print(pd.DataFrame(data = x, columns = features).head())

pca = PCA(n_components=3)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2', 'Principal component 3'])

# principalDf.head(5)
# activity[[0]].head()

#finalDf = pd.concat([principalDf, activity[['0']]], axis = 1)
# print(finalDf.head(5))
# normal = pd.DataFrame(data = x)
# print(normal.head())
# normal.to_csv('./datas/normalize.csv')
principalDf.to_csv('./datas/test2_feature.csv')
plt.semilogy(principalDf, '--o')
#plt.semilogy(x, '--o')
plt.title('Feature after PCA')
plt.show()


#visualise
#
# fig = plt.figure(figsize = (8,8))
# ax = fig.add_subplot(1,1,1)
# ax.set_xlabel('Principal Component 1', fontsize = 15)
# ax.set_ylabel('Principal Component 2', fontsize = 15)
# ax.set_title('2 Component PCA', fontsize = 20)
#
#
# targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
# colors = ['r', 'g', 'b']
# for target, color in zip(targets,colors):
#     indicesToKeep = finalDf['Number of steps'] == target
#     ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
#                , finalDf.loc[indicesToKeep, 'principal component 2']
#                , c = color
#                , s = 50)
# ax.legend(targets)
# ax.grid()