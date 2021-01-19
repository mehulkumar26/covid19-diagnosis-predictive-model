# COVID19 Diagnosis Predictive Model

## Introduction
Designed and implemented a ML classification prediction model using Support Vector Machine (SVM) algorithm. The model is trained using COVID 19 symptoms dataset with features like age, fever, cough, etc. and predicts whether an individual is COVID 19 positive or negative.

## Methodology

### Libraries Used: 
* NumPy 
* Pandas 
* Sklearn 
* Seaborn 
* Matplotlib.pyplot

### Support Vector Machine
Support Vector Machine or SVM is one of the most popular Supervised Learning algorithms, which is used for Classification as well as Regression problems. However, in this project it is used for Classification problems. The goal of the SVM algorithm is to create the best line or decision boundary that can segregate n-dimensional space into classes so that we can easily put the new data point in the correct category in the future. This best decision boundary is called a hyperplane.

### Splitting the data into training and test set
The train-test split procedure is used to estimate the performance of machine learning algorithms when they are used to make predictions on data not used to train the model. It is a fast and easy procedure to perform, the results of which allow you to compare the performance of machine learning algorithms for your predictive modeling problem. 

### Predicting the test set result
To predict the output of the set, a new vector y_pred is created. Now we need to compare the y_pred and y_test to check that how accurate is the prediction.


