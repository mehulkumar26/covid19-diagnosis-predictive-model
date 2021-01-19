#### Covid19 Diagnosis Predictive Model

## Introduction
Designed and implemented a ML classification prediction model using Support Vector Machine (SVM) algorithm. The model is trained using COVID 19 symptoms dataset with features like age, fever, cough, etc. and predicts whether an individual is COVID 19 positive or negative.

## Meathodology 
# Data Cleaning
We will remove all the pickups and drop off which are outside our selected region. We will do this by checking the longitude and latitude. As we are picking New York city we can see that there are many data points which are outside the region. All these points will be removed as a part of the data cleaning process.
# Clustering and Segmentation
Using the K-Means Clustering Algorithm we have divided NY in regions. We  have created clusters of the same size using K-means. Here clusters size represent no. of points, not the area.As there are large no. of pickup in Manhattan so the cluster size will be small as compared to the outskirts of NYC where the cluster size will be large.
# Time Binning
We have converted the time which in regular format to Unix timestamp and divide it by 600 to make 10 min bins. 
# Regression Model
We have used 3 regression models:
Linear regression,
Random Forest Regression and
XGBoost Regression


