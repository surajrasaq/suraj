"""
==========================================
One-class SVM with non-linear kernel (RBF)
==========================================

An example using a one-class SVM for novelty detection.

:ref:`One-class SVM <svm_outlier_detection>` is an unsupervised
algorithm that learns a decision function for novelty detection:
classifying new data as similar or different to the training set.
"""
print(__doc__)
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
from sklearn import svm
from sklearn import cross_validation
import pandas as pd


activity = pd.read_csv('./step_data/walk.csv',  delimiter = ',')

#activity.drop(activity.columns[1], axis=1)
#activity[1] = pd.to_datetime(activity.iloc[1])


X = np.array(activity.iloc[:,[1,]])
y = np.array(activity.iloc[:, 3])
y = y.astype(np.integer)
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=.3, random_state= 0)

clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(X_train, y_train)

# confidence = clf.score(X_test, y_test)
# print(confidence)

#pred = cm(y_test, X_test , binary = False)
pred = clf.predict( X_test)
print('prediction',+ pred)


#Specify keyword arguments to be passed to underlying plotting functions
scatter_kwargs = {'s': 120, 'edgecolor': None, 'alpha': 0.7}
contourf_kwargs = {'alpha': 0.2}
scatter_highlight_kwargs = {'s': 120, 'label': 'Test data', 'alpha': 0.7}

plot_decision_regions(X,y, pred, res= 0.2, legend=4,X_highlight= X_test,
                       scatter_kwargs=scatter_kwargs,
                       contourf_kwargs=contourf_kwargs,
                       scatter_highlight_kwargs=scatter_highlight_kwargs
                      )
plt.title('LDA Prediction with Test Data Highlighted in Circle')


#
# label_dict = ('0','1','2','3','4','Standing','Walking','Football','Climbing','Tram')
# #
# plt.legend(label_dict, loc = 'lower right')
plt.show()







