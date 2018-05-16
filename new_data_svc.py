# Author Surajudeen Abdulrasaq

# University of Lyon/University Jean Monnet France

"""
===============================================
One-class SVM for Ambulation Classification
==============================================

"""


print(__doc__)
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
from sklearn import svm
from sklearn import cross_validation
import pandas as pd
import matplotlib.font_manager



activity = pd.read_csv('./datas/novin_feature.csv',  delimiter = ',')
# activity.drop(activity.columns('activity_begin'),1, inplace= True)
# activity.drop(activity['activity_end'],1, inplace= True)
#
activity1 = pd.read_csv('./datas/test_feature.csv', delimiter=',')
activity1.dropna(inplace= True)


# Decision Boundry
xx, yy = np.meshgrid(np.linspace(-5, 5, 500), np.linspace(-5, 5, 500))

X = np.array(activity.iloc[:,1:])

X_train = np.array(activity.iloc[:,[1,2]])

X_test = np.array(activity.iloc[:,[2,3]])


# fit the model
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(X_train)


# Predict new test-set
pred_new = clf.predict(X_test)
y = pd.DataFrame(data=pred_new)
y_pred = np.array(y)
print(pred_new)

#estimate error rate in predicting

test_error = pred_new[pred_new == -1].size

print(test_error)

# plot the line, the points, and the nearest vectors to the plane
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.title(" One-Class SVM with NEW TEST DATA")
plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.copper)
a = plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='darkred')
plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors='palevioletred')

s = 10
b1 = plt.scatter(X_train[:, 0], X_train[:, 1], c='gold', s=s, edgecolors='k')
b2 = plt.scatter(X_test[:, 0], X_test[:, 1], c = pred_new,  s = 30,edgecolors='k',  cmap='Blues')
c = plt.scatter(y_pred[:,0], y_pred[:,0],c = 'azure', s= 0)

plt.axis('tight')
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.legend([a.collections[0], b1, b2, c],
           ["learned edge", "Training data",
            "Test sets", "Anomally observations"],
           loc="upper left",
           prop=matplotlib.font_manager.FontProperties(size=11))
plt.xlabel(
    " errors rate at test time: %d/100 ; "

    % ( test_error))
plt.show()
