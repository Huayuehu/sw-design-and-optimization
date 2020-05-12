# -*- coding: utf-8 -*-

import numpy as np

#knn分类函数，输入训练样本，训练样本标签，测试样本(为ndarray)，k值（k默认为3）；返回预测标签
def KNN(traindata,trainlabels,testdata,k=3):
    #计算距离，存放在dist中，每一行表示测试样本与所有训练样本的距离
    num_train=traindata.shape[0]
    num_test=testdata.shape[0]
    dist=np.zeros((num_test,num_train))
    for i in range(num_test):
        dist[i]=np.reshape(np.sqrt(np.sum(np.square(testdata[i]-traindata),axis=1)),[1,num_train])
    #找到每一行中从小到大排序后前k个值所对应的原来的索引,对应的标签给close_k
    #统计这些索引中出现次数最多的那个数为预测样本类别
    predictlabels=np.zeros((num_test,1))
    for i in range(num_test):
        close_k=trainlabels[np.argsort(dist[i])[:k]]
        predictlabels[i]=np.argmax(np.bincount(close_k))

    return predictlabels