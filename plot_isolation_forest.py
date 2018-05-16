"""
===================================================
IsolationForest for Ambulation Classification
===================================================


"""
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
import pandas as pd
import pickle

rng = np.random.RandomState(42)
activity = pd.read_csv('./datas/novin_feature.csv',  delimiter = ',')

activity1 = pd.read_csv('./datas/test_feature.csv', delimiter=',')
activity1.dropna(inplace= True)
#activity.drop([0])



X = np.array(activity.iloc[:,1:])

X_train = np.array(activity.iloc[:,[1,2]])

X_test = np.array(activity.iloc[:,[2,3]])


# fit the model
clf = IsolationForest(max_samples=100, random_state=rng)
clf.fit(X_train)

# Predict new test-set
pred_new = clf.predict(X_test)
y = pd.DataFrame(data=pred_new)
y_pred = np.array(y)
print(pred_new)
#estimate error rate in predicting

test_error = pred_new[pred_new == -1].size

print(test_error)
#print(y_pred_test)
#we use pickle to save our classifier so next time we dont have to re-train
# with open('isolation.pickle', 'wb') as f:
#     pickle.dump(clf,f)

# #load pickle you dont have to re-train
# load_pickle = open('isolation.pickle', 'rb')
# clas_fier = pickle.load(load_pickle)
# #predict new test set
# #y_pred_train = clas_fier.predict(X_train)
# picle_test = clas_fier.predict(X_test)



# plot the line, the samples, and the nearest vectors to the plane
xx, yy = np.meshgrid(np.linspace(-5, 5, 50), np.linspace(-5, 5, 50))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.title("Isolation forest with completely new TEST DATA")
plt.contourf(xx, yy, Z, cmap=plt.cm.Reds)

color = 'green'
b1 = plt.scatter(X_train[:, 0], X_train[:, 1], c= 'gold' ,s = 10, edgecolors= 'k')
b2 = plt.scatter(X_test[:, 0], X_test[:, 1], c = pred_new,  s = 30,edgecolors='k',  cmap='Blues')

c = plt.scatter(y_pred[:,0], y_pred[:,0],c = 'azure', s= 0)
plt.axis('tight')
plt.xlim((-5, 5))
plt.ylim((-5, 5))


#
plt.legend([b1, b2,c],
           ["training data","test data",
             "Anomaly Observation"],
           loc="upper left")
plt.xlabel(
    " errors rate at test time: %d/100 ; "

    % ( test_error))
plt.show()
