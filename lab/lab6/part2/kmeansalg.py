# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

'''
选择K个点作为初始质心  
repeat  
    将每个点指派到最近的质心，形成K个簇  
    重新计算每个簇的质心
until 簇不发生变化或达到最大迭代次数
'''

'''
params: 
data
n -- 80 数据量
m -- 2 数据维度
k -- 4 clusters
'''
def kmeans(data, n, m, k, plt):
    # 获取4个随机数 rand_array里是4个index
    # 乘以数据集大小——>数据集中随机的4个点作为初始中心点用center装
    rand_array = np.random.random(size = k)
    rand_array = np.floor(rand_array * n) # ceiling向上取整，floor向下取整
    rand_array = rand_array.astype(int)
    center = data[rand_array] # center里装了四个点的坐标
    print('初始center=\n', center)

    # 1行80列的0数组，cluster_label用来存每个点距离最近的center
    cluster_label = np.zeros([n], np.int) # np.empty()生成的数组里面填充的是null，np.zeros()里面填充的全为0
    flag = True
    count = 0 # to store the numbers of iteration

    while flag:
        count = count + 1

        # 过一遍data中的每个点，给它们选择一个cluster归属
        for i in range(n):
            # tmp里最初装的是第i行data分别减去四个center点的delta，i.e也是四个点
            # 实现 (xi - x)^2 + (yi - y)^2 之后tmp里装的就变成了4个数
            tmp = data[i] - center
            tmp = np.square(tmp)
            tmp = np.sum(tmp, axis = 1) # axis = 1表示按行求和
            # 取最近的给该点“染色”，i.e标记每个样本所属的类
            cluster_label[i] = np.argmin(tmp) # np.argmin()拿到min(tmp)的index

        flag = False # 走到这儿默认结束循环，除非下面更新了center则重新进循环

        # 计算更新每个类的中心点
        # 找到属于该类的所有样本点
        # axis = 0表示按列求平均值，得到第i类的新的中心点
        # 如果新旧center的差距很小，看做相等，center[i]不更新；
        # 否则把newcenter更新成center[i]，flag置true，再来一次循环
        for i in range(k):
            club = data[cluster_label == i] # club里装的是属于该cluster的所有data
            newcenter = np.mean(club, axis = 0)
            delta_center = np.abs(center[i] - newcenter)
            if np.sum(delta_center, axis = 0) > 1e-4:
                center[i] = newcenter
                flag = True

        # 四个类的center都更新完
        print('new center=\n', center)
    # center没有再更新了，结束循环
    print('程序结束，迭代次数：', count)

    # 按cluster打印图表，因为每调用一次showtable，颜色会变，所以可区分出来
    for i in range(k):
        club = data[cluster_label == i] # club里装的是属于该cluster的所有data
        showtable(club, plt)
    # 最后 把四个center打出来，最后打印因为center也要和data区分开
    showtable(center, plt)


def showtable(data, plt):
    x = data.T[0]
    y = data.T[1]
    plt.scatter(x, y)


if __name__ == "__main__":
    csv = pd.read_csv("KmeansData.txt")
    showtable(csv.values, plt) # 打印原始数据
    kmeans(csv.values, 80, 2, 4, plt)
    plt.show()