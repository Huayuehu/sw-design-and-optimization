import numpy as np
import matplotlib.pyplot as plt
import sys
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier

# extract the data from the downloaded pickle files and return a dictionary
def unpickle(file):
	import pickle
	with open(file, 'rb') as fo:
		dict = pickle.load(fo, encoding = 'bytes')
	return dict


"""
traindata: N x 3072 = N x 3 x 32 x 32
trainlabels: N x 1
testdata: (1000-N) x 3072 = (1000-N) x 3 x 32 x 32
testlabels: (1000-N) x 1
"""
def split_images(N, path_to_data):
	batch_dict = unpickle(path_to_data)
	all_data = batch_dict[b'data'].astype('float')
	all_labels = np.array(batch_dict[b'labels'])
	# split into training and testing set
	traindata = all_data[:N]
	trainlabels = all_labels[:N]
	testdata = all_data[N:1000]
	testlabels = all_labels[N:1000]
	img_train = traindata.reshape(N, 3, 32, 32) # RGB 3 channels，32 * 32
	img_test = testdata.reshape(1000 - N, 3, 32, 32)
	return img_train, img_test, trainlabels, testlabels


def rgb_to_gray(rgb):
	r, g, b = rgb[0,:,:], rgb[1,:,:], rgb[2,:,:]
	gray = 0.299 * r + 0.587 * g + 0.114 * b
	return gray


def knn_classify(traindata, trainlabels, testdata, K):
	# to calculate Manhattan distance
	num_train = traindata.shape[0]
	num_test = testdata.shape[0]
	distances = np.zeros((num_test,num_train))
	for i in range(num_test):
		distance_abs = np.abs(testdata[i] - traindata)
		distance_sum = np.sum(distance_abs, axis = 1)
		distances[i] = np.reshape(distance_sum, [1, num_train])
	predict_labels = np.zeros((num_test, 1))
	for i in range(num_test):
		sorted_distance_indexes = np.argsort(distances[i])
		closest_k = trainlabels[sorted_distance_indexes[:K]]
		predict_labels[i] = np.argmax(np.bincount(closest_k))
	# return the label corresponding to every test sample
	return predict_labels 


if __name__ == "__main__":
	K = int(sys.argv[1])
	D = int(sys.argv[2])
	N = int(sys.argv[3])
	path_to_data = str(sys.argv[4])

	# split images from dataset
	img_train, img_test, trainlabels, testlabels = split_images(N, path_to_data)

	# preprocessing
	gray_train_data = []
	gray_test_data = []
	for i in range(N):
		img_gray = rgb_to_gray(img_train[i])
		gray_train_data.append(img_gray)
	for i in range(1000 - N):
		img_gray = rgb_to_gray(img_test[i])
		gray_test_data.append(img_gray)
	img_train_vector = []
	img_test_vector = []
	for i in range(N):
		vector = gray_train_data[i].reshape(32 * 32)
		img_train_vector.append(vector)
	for i in range(1000 - N):
		vector = gray_test_data[i].reshape(32 * 32)
		img_test_vector.append(vector)

	# PCA
	pca = PCA(n_components = D, svd_solver = 'full') # create a pca model reducing dimension to  D dimensions
	train_feature = pca.fit_transform(np.array(img_train_vector)) # fit the pca model with img_train_vector and apply dimension reduction
	test_feature = pca.transform(np.array(img_test_vector)) # apply dimension reduction to img_test_vector

	# knn classifier
	predict_labels = knn_classify(train_feature, trainlabels, test_feature, K)
	fout1 = open('knn_results.txt','w')
	for i in range(1000 - N):
		fout1.write(str(int(predict_labels[i])) + " " + str(testlabels[i]) + "\n")
	fout1.close()

	# verify with Sklearn
	knn = KNeighborsClassifier(n_neighbors = K, p = 1)
	knn.fit(train_feature, trainlabels)
	sklearn_labels = knn.predict(test_feature)
	fout2 = open('knn_results_sklearn.txt','w')
	for i in range(1000 - N):
		fout2.write(str(sklearn_labels[i]) + " " + str(testlabels[i]) + "\n")
	fout2.close()

	# num_test = len(predict_labels)
	# num_right = 0
	# for i in range(num_test):
	# 	if predict_labels[i] == testlabels[i]:
	# 		num_right = num_right + 1
	# accuracy1 = round((num_right / num_test) * 100, 2)
	# print("Testing acc: ", accuracy1, "%.")


