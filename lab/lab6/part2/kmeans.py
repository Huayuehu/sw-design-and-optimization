import struct
import sys
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def load_mnist():
    # read train image file
    with open('./mnist/train-images-idx3-ubyte', 'rb') as imgpath:
        imgdata = imgpath.read();

        offset = 0
        fmt_header = '>iiii'
        magic_number, num_images, num_rows, num_cols = struct.unpack_from(fmt_header, imgdata, offset)

        offset += struct.calcsize(fmt_header)
        fmt_image = '>784B'
        image = np.empty((num_images, num_rows, num_cols))
        for i in range(num_images):
            image[i] = np.array(struct.unpack_from(fmt_image, imgdata, offset)).reshape((28, 28))
            offset += struct.calcsize(fmt_image)
        images = np.array(image).reshape(60000, 784)

    return images


def normalization(dataset):
    # normed_data to store normalized data
    normed_data = np.empty((dataset.shape[0],dataset.shape[1]))
    for i in range(dataset.shape[1]):
      normed_data[:,i] = dataset[:,i] / 255
    return normed_data


"""
Initialize with input.txt
"""
def initial_center_func1():
    fin = open('input.txt','r')
    center_lines = fin.readlines()
    for i in range(7):
        center_lines[i] = center_lines[i].split(",") 
    center_data = np.array(center_lines)
    center_data = center_data.astype(float)
    fin.close()
    return center_data


"""
Initialize with random number
"""
def initial_center_func2(N, dataset):
    center_data = np.empty((7, dataset.shape[1]))
    rand = random.sample(range(0, N), 7)
    for i in range(len(rand)):
        center_data[i] = dataset[rand[i]]
    return center_data


"""
Params: dataset stores all the data information for the training dataset
        centers stores all 7 center points
        N is the number of training images
        k is the number of clusters, in this case is 7
Returns the cluster label for each image
"""
def kmeans_cluster_labeling(dataset, centers, N, k):
    cluster_label = np.zeros([N], np.int)
    flag = True
    count = 0 # to store the numbers of iteration

    while flag:
        # For each data in dataset, calculate the distance between the data and every center
        # it belongs to the cluster with the shortest distance
        for i in range(N):
            distances = dataset[i] - centers
            distances = np.square(distances)
            distances = np.sum(distances, axis = 1)
            classification = np.argmin(distances) # np.argmin() to get index of min(distances)
            cluster_label[i] = classification

        flag = False # end the loop unless a new center is updated below

        # Check whether the centers should be updated or not
        for i in range(k):
            club = dataset[cluster_label == i]
            newcenter = np.mean(club, axis = 0)
            delta_center = np.abs(centers[i] - newcenter)
            if np.sum(delta_center, axis = 0) > 1e-4:
                centers[i] = newcenter
                flag = True

    # when no more change for centers, return
    return cluster_label


if __name__ == '__main__':
    # minist dataset
    train_images = load_mnist()
    N = int(sys.argv[1])
    train_image = normalization(train_images[0:N])

    # obtain initial centers
    flag_of_reading = int(sys.argv[2])
    if flag_of_reading == 1 :
        center_data = initial_center_func1()
    elif flag_of_reading == 0:
        center_data = initial_center_func2(N, train_image)

    # K-means clustering
    labels = kmeans_cluster_labeling(train_image, center_data, N, 7)
    fout = open('results.txt','w')
    for i in range(N):
        fout.write(str(labels[i]) + "\n")
    fout.close()
