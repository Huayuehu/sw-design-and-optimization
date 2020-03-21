# -*- coding: utf-8 -*-
import struct
import numpy as np
import sys
import random
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
    normed_data = np.empty((dataset.shape[0],dataset.shape[1]))
    for i in range(dataset.shape[1]):
      normed_data[:,i] = dataset[:,i] / 255
    return normed_data


def initial_center_func1():
    fin = open('input.txt','r')
    center_lines = fin.readlines()
    for i in range(7):
        center_lines[i] = center_lines[i].split(",") 
    center_data = np.array(center_lines)
    center_data = center_data.astype(float)
    fin.close()
    return center_data


def initial_center_func2(N, dataset):
    center_data = np.empty((7, dataset.shape[1]))
    rand = random.sample(range(0, N), 7)
    for i in range(len(rand)):
        center_data[i] = dataset[rand[i]]
    return center_data

"""
center_data中已经装了7个初始center的所有信息
"""
def kmeans_cluster_labeling(dataset, centers, N, k):
    cluster_label = np.zeros([N], np.int)
    flag = True
    count = 0 # to store the numbers of iteration

    while flag:
        count = count + 1

        # 对于每一个data，算出它们与每个center之间的距离装在distances里，最短的distances对于的index就是归属的cluster
        for i in range(N):
            distances = dataset[i] - centers
            distances = np.square(distances)
            distances = np.sum(distances, axis = 1)
            classification = np.argmin(distances) # np.argmin()拿到min(distances)的index
            # print("for ", i, "th in ", N, " the classification is ", classification)
            cluster_label[i] = classification

        flag = False # 走到这儿默认结束循环，除非下面更新了center则重新进循环

        # 计算更新每个类的中心点
        # 找到属于该类的所有样本点
        # axis = 0表示按列求平均值，得到第i类的新的中心点
        # 如果新旧center的差距很小，看做相等，centers[i]不更新；
        # 否则把newcenter更新成centers[i]，flag置true，再来一次循环
        for i in range(k):
            club = dataset[cluster_label == i]
            newcenter = np.mean(club, axis = 0)
            delta_center = np.abs(centers[i] - newcenter)
            if np.sum(delta_center, axis = 0) > 1e-4:
                centers[i] = newcenter
                flag = True

    # centers不再更新了，结束循环，返回相应的labels和new centers
    print('程序结束，迭代次数：', count)
    return cluster_label, centers


if __name__ == '__main__':
    # MNIST dataset
    train_images = load_mnist()
    N = int(sys.argv[1])
    train_image = normalization(train_images[0:N])

    # Obtain initial centers
    flag_of_reading = int(sys.argv[2])
    if flag_of_reading == 1 :
        center_data = initial_center_func1()
    else:
        if flag_of_reading == 0:
            center_data = initial_center_func2(N, train_image)
        else:
            print("Please enter 1 or 0 next to N.")

    # K-means clustering
    labels, centers = kmeans_cluster_labeling(train_image, center_data, N, 7)
    fout = open('results.txt','w')
    for i in range(N):
        fout.write(str(labels[i]) + "\n")
    fout.close()
