import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('pandemic_data.csv',dtype = float, delimiter=',')
data.head()
data.describe()
sns.pairplot(data=data[['Age','Sex','Fever','Fatigue','Target']], hue='Target')
sns.pairplot(data=data[['Cough','SOB','Target']], hue='Target')
train = data.drop('Target',axis = 1)
train.head()
Target = data.Target
Target.head()
X_train, X_test, Y_train, Y_test = train_test_split(train, Target, test_size=0.3)
print("X_train size ==>", X_train.shape)
print("Y_train size ==>", Y_train.shape)
print("X_test size ==>", X_test.shape)
print("Y_test size ==>", Y_test.shape)
clf = svm.SVC(kernel='linear')
clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(Y_test, Y_pred))
print("Precision:",metrics.precision_score(Y_test, Y_pred))
print("Recall:",metrics.recall_score(Y_test, Y_pred))
