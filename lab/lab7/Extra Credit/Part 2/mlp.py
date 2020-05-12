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

	with open('./mnist/train-labels-idx1-ubyte', 'rb') as labelpath:
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
	        labels[i] = struct.unpack_from(fmt_image, bin_data, offset)[0]
	        offset += struct.calcsize(fmt_image)

    return images, labels

    # # 读取图片
    # with open('./mnist/train-labels-idx1-ubyte', 'rb') as lbpath:
    #     magic, n = struct.unpack('>II',lbpath.read(8))
    #     labels = np.fromfile(lbpath,dtype=np.uint8)

    # # 将each image reshape to 1-D space with shape 784
    # with open('./mnist/train-images-idx3-ubyte', 'rb') as imgpath:
    #     # 数据结构中前4行的数据类型都是32-bit integer，format格式为i，我们需要读取前4行数据，所以需要4个i
    #     magic, num, rows, cols = struct.unpack('>IIII',imgpath.read(16))
    #     images = np.fromfile(imgpath,dtype=np.uint8).reshape(len(labels), 784)

    # return images, labels

    # def decode_idx1_ubyte(idx1_ubyte_file):



def normalization(dataset):
    normed_data = np.empty((dataset.shape[0],dataset.shape[1]))
    for i in range(dataset.shape[1]):
      normed_data[:,i] = dataset[:,i] / 255
    return normed_data


if __name__ == '__main__':
    # MNIST dataset
    train_images = load_mnist()
    N = int(sys.argv[1])
    train_image = normalization(train_images[0:N])