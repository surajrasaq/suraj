# Author Surajudeen Abdulrasaq

# University of Lyon/University Jean Monnet France

"""
==========================================
Classification with LDA
==========================================

"""

from mlxtend.plotting import plot_decision_regions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import cross_val_predict, KFold


activity = pd.read_csv('./step_data/walk.csv',  delimiter = ',')


# activity[['0']] =  activity[['0']].replace([0,1,2,3,4],[ 'Standing', 'Walking','Football', 'Climbing','Tram'])
# #act_feature.to_csv('./datas/act_feature.csv')
#print(activity.head())

X = np.array(activity.iloc[:,[1,3]])
y = np.array(activity.iloc[:, 3])

#print(len(activity))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.4, random_state= 0)

LDA = LinearDiscriminantAnalysis(n_components= 2 )
LDA.fit_transform(X_train, y_train)

confidence = LDA.score(X_test, y_test)
print(confidence)

#pred = cm(y_test, X_test , binary = False)
pred = LDA.predict(X_test)
print('prediction',+ pred)

# cv = KFold(n_splits=2)
#
# k_validate = cross_val_predict(LDA, X,y, cv = cv)
# print(k_validate)

#Specify keyword arguments to be passed to underlying plotting functions
scatter_kwargs = {'s': 120, 'edgecolor': None, 'alpha': 0.7}
contourf_kwargs = {'alpha': 0.2}
scatter_highlight_kwargs = {'s': 120, 'label': 'Test data', 'alpha': 0.7}

plot_decision_regions(X,y, LDA, res= 0.2, legend=4,filler_feature_values={3: 1},X_highlight=X_test,
                       scatter_kwargs=scatter_kwargs,
                       contourf_kwargs=contourf_kwargs,
                       scatter_highlight_kwargs=scatter_highlight_kwargs
                      )
plt.title('LDA Classification after PCA, Test data highlighted')
#
#label_dict = ('0','1','2','3','4','Standing','Walking','Football','Climbing','Tram')
# #
plt.legend( loc = 'upper right')
plt.show()

