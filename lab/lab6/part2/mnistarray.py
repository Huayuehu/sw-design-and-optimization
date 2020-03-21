# -*- coding: utf-8 -*-
import struct
import numpy as np
import matplotlib.pyplot as plt

# 1. n x m 的Numpy array, n样本数, m特征数
# 2. 包含相应手写数字的类标签的数组(整数0-9)
def load_mnist():
    # 读取图片
    with open('./mnist/train-labels-idx1-ubyte', 'rb') as lbpath:
        magic, n = struct.unpack('>II',lbpath.read(8))
        labels = np.fromfile(lbpath,dtype=np.uint8)

    # 将each image reshape to 1-D space with shape 784
    with open('./mnist/train-images-idx3-ubyte', 'rb') as imgpath:
        # 数据结构中前4行的数据类型都是32-bit integer，format格式为i，我们需要读取前4行数据，所以需要4个i
        magic, num, rows, cols = struct.unpack('>IIII',imgpath.read(16))
        images = np.fromfile(imgpath,dtype=np.uint8).reshape(len(labels), 784)

    return images, labels

# fig, ax = plt.subplots(nrows=2,ncols=5,sharex=True,sharey=True, )

# ax = ax.flatten()
# X_train,y_train = load_mnist('./mnist/')
# for i in range(10):
#     # reshape成之前的2-D space with shape 28 * 28
#     img = X_train[y_train == i][0].reshape(28, 28)
#     # img = X_train[y_train == 6][i].reshape(28, 28)
#     ax[i].imshow(img, cmap='Greys', interpolation='nearest')

# ax[0].set_xticks([])
# ax[0].set_yticks([])
# plt.show()

if __name__ == '__main__':
    x_train,y_train = load_mnist()

    # 查看前十个数据及其标签以读取是否正确
    for i in range(9, 10):
        print(int(y_train[i]))
        plt.imshow(x_train[i].reshape(28, 28), cmap='gray')
        plt.pause(0.000001)
        plt.show()
    print('done')
