# -*- coding: utf-8 -*-
import numpy as np
import struct
import matplotlib.pyplot as plt

train_images_idx3_ubyte_file = './mnist/train-images-idx3-ubyte'
train_labels_idx1_ubyte_file = './mnist/train-labels-idx1-ubyte'

def decode_idx3_ubyte(idx3_ubyte_file):
    bin_data = open(idx3_ubyte_file, 'rb').read()

    # 解析文件头信息
    offset = 0
    fmt_header = '>iiii'
    magic_number, num_images, num_rows, num_cols = struct.unpack_from(fmt_header, bin_data, offset)

    # 解析数据集
    image_size = num_rows * num_cols
    # 获得数据在缓存中的指针位置，读取了前4行之后，指针位置（即offset）指向0016
    offset += struct.calcsize(fmt_header)
    # 图像数据像素值的类型为unsigned char型，对应的format格式为B。
    # 这里还有加上图像大小784，是为了读取784个B格式数据，如果没有则只会读取一个值（即一副图像中的一个像素值）
    fmt_image = '>784B'
    images = np.empty((num_images, num_rows, num_cols))

    for i in range(num_images):
        images[i] = np.array(struct.unpack_from(fmt_image, bin_data, offset)).reshape((num_rows, num_cols))
        offset += struct.calcsize(fmt_image)
    return images


def decode_idx1_ubyte(idx1_ubyte_file):
    bin_data = open(idx1_ubyte_file, 'rb').read()

    # 解析文件头信息
    offset = 0
    fmt_header = '>ii'
    magic_number, num_images = struct.unpack_from(fmt_header, bin_data, offset)

    # 解析数据集
    offset += struct.calcsize(fmt_header)
    fmt_image = '>B'
    labels = np.empty(num_images)
    for i in range(num_images):
        labels[i] = struct.unpack_from(fmt_image, bin_data, offset)[0]
        offset += struct.calcsize(fmt_image)
    return labels


if __name__ == '__main__':
    train_images = decode_idx3_ubyte(train_images_idx3_ubyte_file)
    train_labels = decode_idx1_ubyte(train_labels_idx1_ubyte_file)

    # 查看前十个数据及其标签以读取是否正确
    for i in range(10):
        print(int(train_labels[i]))
        plt.imshow(train_images[i], cmap='gray')
        plt.pause(0.000001)
        plt.show()
    print('done')
