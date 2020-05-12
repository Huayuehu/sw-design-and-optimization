# -*- coding: utf-8 -*-
import KNN
from numpy import*
data,labels = KNN.createDataSet()

# print '测试模型分类样本数据,结果是否和样本中的分类一致'
# input = [0.5, 1, 1, 1]
# print '\n分类结果:'+ KNN.classify(input, data, labels, 2)

print '测试新数据'
input = [1, 0.1, 0.9, 1]
print input
print '分类结果:'+ KNN.classify(input, data, labels, 2)