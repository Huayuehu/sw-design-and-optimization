# -*- coding: utf-8 -*-
import sys
import struct
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
import torchvision


train_images_idx3_ubyte_file = './mnist/train-images-idx3-ubyte'
train_labels_idx1_ubyte_file = './mnist/train-labels-idx1-ubyte'
test_images_idx3_ubyte_file = './mnist/t10k-images-idx3-ubyte'
test_labels_idx1_ubyte_file = './mnist/t10k-labels-idx1-ubyte'


# def decode_idx3_ubyte(idx3_ubyte_file):
#     """
#     :param idx3_ubyte_file: idx3文件路径
#     :return: 数据集
#     """
#     bin_data = open(idx3_ubyte_file, 'rb').read()

#     offset = 0
#     fmt_header = '>iiii'
#     magic_number, num_images, num_rows, num_cols = struct.unpack_from(fmt_header, bin_data, offset)
#     print('Magic Number:%d, Numebr of images: %d, shape of image: %d*%d' % (magic_number, num_images, num_rows, num_cols))

#     offset += struct.calcsize(fmt_header)  #获得数据在缓存中的指针位置，从前面介绍的数据结构可以看出，读取了前4行之后，指针位置（即偏移位置offset）指向0016
#     fmt_image = '>784B'
#     images = np.empty((num_images, num_rows, num_cols))
#     #plt.figure()
#     for i in range(num_images):
#         if (i + 1) % 10000 == 0:
#             print('resolved %d' % (i + 1))
#             print(offset)
#         images[i] = np.array(struct.unpack_from(fmt_image, bin_data, offset)).reshape((num_rows, num_cols))
#         offset += struct.calcsize(fmt_image)
#     return images


# def decode_idx1_ubyte(idx1_ubyte_file):
#     """
#     :param idx1_ubyte_file: idx1文件路径
#     :return: 数据集
#     """
#     bin_data = open(idx1_ubyte_file, 'rb').read()

#     offset = 0
#     fmt_header = '>ii'
#     magic_number, num_images = struct.unpack_from(fmt_header, bin_data, offset)
#     print('Magic Number:%d, Numebr of images: %d' % (magic_number, num_images))

#     offset += struct.calcsize(fmt_header)
#     fmt_image = '>B'
#     labels = np.empty(num_images)
#     for i in range(num_images):
#         if (i + 1) % 10000 == 0:
#             print ('resolved %d' % (i + 1))
#         labels[i] = struct.unpack_from(fmt_image, bin_data, offset)[0]
#         offset += struct.calcsize(fmt_image)
#     return labels

def load_mnist(imgpath, labelpath):
    # read train image file
    with open(imgpath, 'rb') as imgpath:
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
        # images = np.array(image).reshape(60000, 784)

    with open(labelpath, 'rb') as labelpath:
        labeldata = labelpath.read();

        # 解析文件头信息
        offset = 0
        fmt_header = '>ii'
        magic_number, num_images = struct.unpack_from(fmt_header, labeldata, offset)

        # 解析数据集
        offset += struct.calcsize(fmt_header)
        fmt_image = '>B'
        labels = np.empty(num_images)
        for i in range(num_images):
            labels[i] = struct.unpack_from(fmt_image, labeldata, offset)[0]
            offset += struct.calcsize(fmt_image)

    return image, labels


def normalization(dataset):
    normed_data = np.empty((dataset.shape[0],dataset.shape[1]))
    for i in range(dataset.shape[1]):
        normed_data[:,i] = dataset[:,i] / 255
    return normed_data


def activation(in_dim, n_hidden_1, out_dim):
    layer1 = nn.Sequential(nn.Linear(in_dim, n_hidden_1), nn.ReLU(True))


if __name__ == '__main__':
    N = int(sys.argv[1])
    M = int(sys.argv[2])

    # MNIST dataset
    train_images, train_labels = load_mnist(train_images_idx3_ubyte_file, train_labels_idx1_ubyte_file)
    test_images, test_labels = load_mnist(test_images_idx3_ubyte_file, test_labels_idx1_ubyte_file)


    train_images = train_images.reshape(60000, 784)
    test_images = test_images.reshape(10000, 784)

    train_images_normed = normalization(train_images[0:N])
    test_images_normed = normalization(test_images[0:M])

    



    # model = net.activation(28 * 28, 300, 100, 10)


    # # 定义损失函数和优化器
    # criterion = nn.CrossEntropyLoss()
    # optimizer = optim.SGD(model.parameters(), lr=learning_rate)

