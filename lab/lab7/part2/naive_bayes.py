# -*- coding: utf-8 -*-
import numpy as np
import scipy as sp
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import collections


"""
It returns the prior probabilities of the 2 classes 
as per eq-1) by taking the label set y as input.
"""
def pre_prob(y):
    y_dict = collections.Counter(y)
    pre_probab = np.ones(2)
    for i in range(0, 2):
        pre_probab[i] = y_dict[i]/y.shape[0]
    return pre_probab

"""
It is the function that returns the mean and variance 
of all the features for 2 class labels (binary classification), 
given the feature set X and label set y as input.
"""
def mean_var(X, y):
	n_features = X.shape[1]
	m = np.ones((2, n_features))
	v = np.ones((2, n_features))
	n_0 = np.bincount(y)[np.nonzero(np.bincount(y))[0]][0]
	x0 = np.ones((n_0, n_features))
	x1 = np.ones((X.shape[0] - n_0, n_features))
	
	k = 0
	for i in range(0, X.shape[0]):
		if y[i] == 0:
			x0[k] = X[i]
			k = k + 1
	k = 0
	for i in range(0, X.shape[0]):
		if y[i] == 1:
			x1[k] = X[i]
			k = k + 1
        
	for j in range(0, n_features):
		m[0][j] = np.mean(x0.T[j])
		v[0][j] = np.var(x0.T[j])*(n_0/(n_0 - 1))
		m[1][j] = np.mean(x1.T[j])
		v[1][j] = np.var(x1.T[j])*((X.shape[0]-n_0)/((X.shape[0] - n_0) - 1))
	return m, v # mean and variance 

"""
It is the function that returns the posterior probabilities of the test data x 
given class c (eq-2) by taking mean m, variance v and test data x as input.
"""
def prob_feature_class(m, v, x):
    n_features = m.shape[1]
    pfc = np.ones(2)
    for i in range(0, 2):
        product = 1
        for j in range(0, n_features):
            product = product * (1/sqrt(2*3.14*v[i][j])) * exp(-0.5
                                 * pow((x[j] - m[i][j]),2)/v[i][j])
        pfc[i] = product
    return pfc


"""
It is the function that sums up the 3 other functions by using the entities returned by them 
to finally calculate the Conditional Probability of the each of the 2 classes 
given the test instance x (eq-4) 
by taking the feature set X, label set y and test data x as input and returns:
Mean of the 2 classes for all the features
Variance of the 2 classes for all the features
Prior Probabilities of the 2 classes in the dataset
Posterior Probabilities of the test data given each class of the 2 classes
Conditional Probability of each of the 2 classes given the test data
Final Prediction given by Gaussian Naive Bayes Algorithm
"""
def GNB(X, y, x):
    m, v = mean_var(X, y)
    pfc = prob_feature_class(m, v, x)
    pre_probab = pre_prob(y)
    pcf = np.ones(2)
    total_prob = 0
    for i in range(0, 2):
        total_prob = total_prob + (pfc[i] * pre_probab[i])
    for i in range(0, 2):
        pcf[i] = (pfc[i] * pre_probab[i])/total_prob
    prediction = int(pcf.argmax())
    return m, v, pre_probab, pfc, pcf, prediction


# 已经分出了80%训练集和20%测试集
# dataset manipulation
path = 'seeds_dataset.txt'
feature_names = ['area','perimeter','compactness','length-kernel','width-kernel','asymmetry-coefficient','length-kernel-groove']
seeds = pd.read_table(path, header=None, names=feature_names + ['class'], sep='\\s+')
class_names = ['Kama', 'Rosa', 'Canadian']
seeds = pd.concat([seeds[feature_names], pd.DataFrame([class_names[i-1] for i in list(seeds['class'])],  columns=['class'])],axis=1)
# randomly shuffle the samples and split the dataset to 80% training set and 20% test set.
train_data, test_data = train_test_split(seeds, test_size=0.2)


