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
Support Vector Machine or SVM is one of the most popular Supervised Learning algorithms, which is used for Classification as well as Regression problems.  However, in this project, it is used for Classification problems. The data set in the project is small which is why the Support Vector Machine Algorithm is used in the classification model, as it provides the highest accuracy on a small data set.

### Splitting the data into training and test set
The train-test split procedure is used to estimate the performance of machine learning algorithms when they are used to make predictions on data not used to train the model.  The database was split into 30 percent test data set and 60 percent train data set.

### Predicting the test set result
To predict the output of the set, a new vector y_pred is created. A comparison is done between the y_pred and y_test to check that how accurate is the prediction.


