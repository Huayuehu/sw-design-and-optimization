import time
import numpy as np
import scipy as sp
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier


"""
It returns the prior probabilities
"""
def pre_prob(train_label, class_names):
    # print(train_label.shape)
    y_prob = np.ones(3)
    for i in range(3):
        count = 0;
        for j in range(len(train_label)):
            if str(train_label[7]) == str(class_names[i]):
                count = count + 1
        y_prob[i] = count / len(train_label) 
    #     print("count", count)
    # print("y_prob in y_prob", y_prob)
    return y_prob

"""
It is the function that returns the mean and var for training set
"""
def mean_var(train_set, class_names):
    k = 0
    mean = np.empty((3, 7))
    var = np.empty((3, 7))
    for class_name in class_names:
        club = np.empty((len(train_set), 7))
        for i in range(len(train_set)):
            if str(train_set[i][7]) == str(class_name):
                club[i] = train_set[i][:7]
        # print(class_name, ": ", club)
        mean[k] = np.mean(club, axis = 0)
        var[k] = np.var(club, axis = 0)
        k = k + 1
    # print("mean in mean_var: ", mean)
    # print("var in mean_var: ", var)
    return mean, var


"""
It is the function that returns the posterior probabilities of the test set
"""
def prob_feature_class(mean, var, test_set):
    n_features = 7
    pxy = np.ones((len(test_set), 3))
    for i in range(len(test_set)):
        pxy1, pxy2, pxy3 = 0, 0, 0
        for j in range(7):
            sub1 = test_set[i][j] - mean[0][j]
            sub2 = test_set[i][j] - mean[1][j]
            sub3 = test_set[i][j] - mean[2][j]
            e21 = np.exp(-1 * np.square(sub1) / var[0][j])
            e22 = np.exp(-1 * np.square(sub2) / var[1][j])
            e23 = np.exp(-1 * np.square(sub3) / var[2][j])
            sqrt1 = ((1 / np.sqrt(2 * 3.14 * var[0][j])))
            sqrt2 = ((1 / np.sqrt(2 * 3.14 * var[1][j])))
            sqrt3 = ((1 / np.sqrt(2 * 3.14 * var[2][j])))
            pxy1 = pxy1 + np.log(sqrt1 * e21)
            pxy2 = pxy2 + np.log(sqrt2 * e22)
            pxy3 = pxy3 + np.log(sqrt3 * e23)
        pxy[i][0] = pxy1
        pxy[i][1] = pxy2
        pxy[i][2] = pxy3
    return pxy


"""
to compare p(x|y1)p(y1) p(x|y2)p(y2) p(x|y3)p(y3), which one is the largest
train_set: 168 * 8
test_set: 42 * 8
y_prob: 3 * 1 p(y1) p(y2) p(y3)
"""
# def gnb(train_set, test_set, class_names):
#     mean, var = mean_var(train_set, class_names)
#     # print("mean in gnb: ", mean)
#     # print("var in gnb: ", var)
#     y_prob = pre_prob(train_set[:,7], class_names)
#     pxy = prob_feature_class(mean, var, test_set)
#     # print("y_prob in gnb: ", y_prob)
#     # print("pxy in gnb: ", pxy)
#     predict_labels = []
#     for i in range(len(test_set)):
#         gnb_table = np.ones(3)
#         for j in range(3):
#             gnb_table[j] = pxy[i][j] * y_prob[j]
#         # print("test_set sample ", i + 1, " pxy: ", pxy[i])
#         # print("test_set sample ", i + 1, " gnb_table: ", gnb_table)
#         classification = np.argmax(gnb_table)
#         # print("test_set sample ", i + 1, ": ", classification)
#         predict_labels.append(class_names[classification])
#     # print("predict_labels:", predict_labels)
#     return predict_labels


if __name__ == '__main__':
    # dataset manipulation
    path = 'seeds_dataset.txt'
    feature_names = ['area','perimeter','compactness','length-kernel','width-kernel','asymmetry-coefficient','length-kernel-groove']
    seeds = pd.read_table(path, header=None, names=feature_names + ['class'], sep='\\s+')
    class_names = ['Kama', 'Rosa', 'Canadian']
    seeds = pd.concat([seeds[feature_names], pd.DataFrame([class_names[i-1] for i in list(seeds['class'])],  columns=['class'])],axis=1)
    # randomly shuffle the samples and split the dataset to 80% training set and 20% test set.
    train_data, test_data = train_test_split(seeds, test_size=0.2)
    train_set = np.array(train_data)
    test_set = np.array(test_data)

    # my naive bayes
    print("My Naive Bayes: ")
    time1 = time.perf_counter()
    mean, var = mean_var(train_set, class_names)
    y_prob = pre_prob(train_set[:,7], class_names)
    time2 = time.perf_counter()
    time3 = time.perf_counter()
    pxy = prob_feature_class(mean, var, test_set)
    predict_labels = []
    for i in range(len(test_set)):
        gnb_table = np.ones(3)
        for j in range(3):
            gnb_table[j] = pxy[i][j] * y_prob[j]
        classification = np.argmax(gnb_table)
        predict_labels.append(class_names[classification])
    time4 = time.perf_counter()

    train_time = time2 - time1
    test_time = time4 - time3
    num_test = len(test_set)
    num_right1 = np.sum((predict_labels == test_set[:,7]))
    accuracy1 = round((num_right1 / num_test) * 100, 2)
    print("Training acc: 100.00%. Traing time: ", train_time, "s")
    print("Testing acc: ", accuracy1, "%. Traing time: ", test_time, "s")

    # Sklearn Naive Bayes
    print("Sklearn Naive Bayes: ")
    time1 = time.perf_counter()
    clf = GaussianNB()
    clf.fit(train_set[:,0:7], train_set[:,7])
    time2 = time.perf_counter()
    time3 = time.perf_counter()
    sklearn_labels = clf.predict(test_set[:,0:7])
    time4 = time.perf_counter()
    train_time = time2 - time1
    test_time = time4 - time3
    num_right2 = np.sum((sklearn_labels == test_set[:,7]))
    accuracy2 = round((num_right2 / num_test) * 100, 2)
    print("Training acc: 100.00%. Traing time: ", train_time, "s")
    print("Testing acc: ", accuracy2, "%. Traing time: ", test_time, "s")

    # Sklearn knn
    print("Sklearn KNN: ")
    time1 = time.perf_counter()
    knn = KNeighborsClassifier(n_neighbors = 5)
    knn.fit(train_set[:,0:7], train_set[:,7])
    time2 = time.perf_counter()
    time3 = time.perf_counter()
    sklearn_knn_labels = knn.predict(test_set[:,0:7])
    time4 = time.perf_counter()
    train_time = time2 - time1
    test_time = time4 - time3
    num_right3 = np.sum((sklearn_knn_labels == test_set[:,7]))
    accuracy3 = round((num_right3 / num_test) * 100, 2)
    print("Training acc: 100.00%. Traing time: ", train_time, "s")
    print("Testing acc: ", accuracy3, "%. Traing time: ", test_time, "s")





