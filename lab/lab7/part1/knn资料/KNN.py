# -*- coding: utf-8 -*-
from numpy import * # 导入科学计算包
import operator # 导入运算符模块
import json

'''构造训练数据集
data:特征值
labels:每行数据对应的标签
'''
def createDataSet():
    data = array([[1, 1, 1, 1],
                  [0.5, 1, 1, 1],
                  [0.1, 0.1, 0.1, 0.1],
                  [0.5, 0.5, 0.5, 0.5],
                  [1, 0.8, 0.3, 1],
                  [0.6, 0.5, 0.7, 0.5],
                  [1, 1, 0.9, 0.5],
                  [1, 0.6, 0.5, 0.8],
                  [0.5, 0.5, 1, 1],
                  [0.9, 1, 1, 1],
                  [0.6, 0.6, 1, 0.1],
                  [1, 0.8, 0.5, 0.5],
                  [1, 0.1, 0.1, 1],
                  [1, 1, 0.7, 0.3],
                  [0.2, 0.3, 0.4, 0.5],
                  [0.5, 1, 0.6, 0.6]
                  ]);

    labels = ['女神',
              '淑女',
              '丑女',
              '一般型',
              '淑女',
              '一般型',
              '女神',
              '一般型',
              '淑女',
              '女神',
              '丑女',
              '可爱型',
              '可爱型',
              '淑女',
              '丑女',
              '可爱型'
              ]
    return data,labels

'''KNN 分类器
参数说明:
   inX:需要分类的新数据testdata
   data/labels:训练数据集及其对应的标签
   k:选择最近的训练数据数目(一般不超过20)   
'''

def classify(inX,data,labels,k):
    # shape[0] - 向量的行数 shape[1] - 向量的列数
    # shape 返回向量的行数和列数
    dataSetSize = data.shape[0]  # 计算共有多少条训练数据

    # tile(array,reps)将数组array沿维度reps重复,构成新的数组
    # a= [
    #      [1,2],
    #      [3,4]
    #    ]
    # 如tile(a,2)表示a的第一个维度重复2遍,A = [[a],[a]]
    # tile(a,(2,2))表示a的第一个维度重复2遍，第二个维度重复2遍
    # 即tile(array,(rows,cols)) 将array看作单个向量再构造为rows行clos列
    # tile(a,(2,2)) - >
    # A = [
    #      [a,a],
    #      [a,a]
    #     ]

    # 欧式距离计算 [计算输入向量与样本集中各个点的距离]
    #注意:不需要利用循环将输入数据和样本中的每条数据进行距离计算 利用矩阵运算便可一次性求出

    # print '复制输入向量 用于和样本中的每条数据进行计算 [矩阵的加减乘除]'
    # print tile(inX, (dataSetSize, 1))

    # 矩阵的减法 结果:每一项为输入向量和各个样本对应特征点的差值构成的新矩阵
    diffmat = tile(inX,(dataSetSize,1)) - data
    # print '\n相减后:'
    # print diffmat

    sqDiffMat = diffmat**2 #平方 矩阵中每一项都平方
    # print '\n平方后:'
    # print sqDiffMat
    sqDistances = sqDiffMat.sum(axis=1) #axis=1 行向量相加 / axis=0 列向量相加
    # print '\n各个特征点差值相加[即坐标差值相加]:'
    # print sqDistances

    distances = sqDistances**0.5 #开方
    # print '\n距离:'
    # print distances
    sortedDistIndexes = distances.argsort() #从小到大将距离向量排序并返回其索引值
    # print '\n从小到大将距离向量排序并返回其索引值'
    # print sortedDistIndexes

    # 选择距离最小的K个点
    classCount = {} # dict 保存对应标签出现的次数
    for i in range(k):
        voteLabel = labels[sortedDistIndexes[i]] #获得类别标签

        # dict.get(key, default) 返回指定键的值，如果值不在字典中返回default值
        # 对所属的类别标签个数进行统计
        classCount[voteLabel] = classCount.get(voteLabel,0) + 1
    # print '标签出现的次数:'
    # print json.dumps(classCount, encoding="UTF-8", ensure_ascii=False)
    # 排序
    # sorted(iterable, cmp=None, key=None, reverse=False)
    # iterable：是可迭代类型;
    # cmp：用于比较的函数，比较什么由key决定,有默认值，迭代集合中的一项;
    # key：用列表元素的某个属性和函数进行作为关键字，有默认值，迭代集合中的一项;
    # reverse：排序规则. reverse = True 倒序 / reverse = False
    # operator.itemgetter(1) 利用第二个数据域进行排序
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)

    # print '\n排序后:'
    # print json.dumps(sortedClassCount, encoding="UTF-8", ensure_ascii=False)
    # 如: print sortedClassCount ———— [('A', 2), ('B', 1)]

    return sortedClassCount[0][0] #返回次数出现次数最多的标签