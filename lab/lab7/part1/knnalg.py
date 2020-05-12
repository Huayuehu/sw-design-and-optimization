# -*- coding: utf-8 -*-

#从当前路径下的KNN.py载入KNN函数
import numpy as np
import os
import time
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

#将cifar-10中的数据解压成字典类型
def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


#创建训练样本和测试样本
def CreatData():
    #创建训练样本
    #依次加载batch_data_i,并合并到x,y
    x=[]
    y=[]
    for i in range(1,6):
        batch_path='cifar-10-batches-py/data_batch_%d'%(i)
        batch_dict=unpickle(batch_path)
        train_batch=batch_dict[b'data'].astype('float')
        train_labels=np.array(batch_dict[b'labels'])
        x.append(train_batch)
        y.append(train_labels)
    traindata=np.concatenate(x)
    trainlabels=np.concatenate(y)
    testpath=os.path.join('cifar-10-batches-py','test_batch')
    test_dict=unpickle(testpath)
    testdata=test_dict[b'data'].astype('float')
    testlabels=np.array(test_dict[b'labels']) 
    return traindata,trainlabels,testdata,testlabels


#knn分类函数，输入训练样本，训练样本标签，测试样本(为ndarray)，k值；返回预测标签
def KNN(traindata,trainlabels,testdata,k=3):
    #计算距离，存放在distances中，每一行表示测试样本与所有训练样本的距离
    num_train=traindata.shape[0]
    num_test=testdata.shape[0]
    distances=np.zeros((num_test,num_train))
    for i in range(num_test):
        distance_square = np.square(testdata[i] - traindata)
        distance_sum = np.sum(distance_square, axis = 1)
        distance_sqrt = np.sqrt(distance_sum)
        distances[i]=np.reshape(distance_sqrt, [1, num_train])
    predictlabels=np.zeros((num_test,1))
    for i in range(num_test):
        sorted_distance_indexes = np.argsort(distances[i])
        closest_k = trainlabels[sorted_distance_indexes[:k]]
        predictlabels[i] = np.argmax(np.bincount(closest_k))
    # 返回每个test样本对应的label
    return predictlabels 


#创建训练样本和测试样本
traindata1,trainlabels1,testdata1,testlabels1 = CreatData()

# 取前10000个当做training data， 5000当做test data
num_train=1000
num_test=10
traindata=traindata1[:num_train]
trainlabels=trainlabels1[:num_train]
testdata=testdata1[:num_test]
testlabels=testlabels1[:num_test]

#用PCA变换
#pca=PCA(n_components=307,copy=True)
#num_pca=pca.n_components
#pca_traindata=pca.fit_transform(traindata)
#print(num_pca)
#print(pca_traindata.shape)

#记录最高精度max_acc,以及对应的HOG尺寸max_acc_cellsize和K值max_acc_K
max_acc=0
max_acc_n_components=0
max_acc_k=0

#设置不同的k
# k_choice=[5,10,15,20,40,100]
k_choice=[10]
for k_c in k_choice:
    print('\n\nk=',k_c)
    #设置不同的pca成分数
    # num_components=[100,700,1000,2000,3000,3072]
    num_components=[1, 5] # 不同的降维之后的维度
    #对应精度
    size_accuracy=[]

    for num_c in num_components:
        #提取训练样本的PCA特征
        pca=PCA(n_components=num_c,copy=True) # 创建一个pca model
        pca_traindata=pca.fit_transform(traindata) # fit the pca model with traindata and 降维
        #提取测试样本的PCA特征
        pca_testdata=pca.fit_transform(testdata)
    
        #预测标签
        predictlabels=KNN(pca_traindata,trainlabels,pca_testdata,k=k_c)
        testlabels=np.reshape(testlabels,[num_test,1]) # 查找testlabel用来看预测的label和真实label的预测精度
        #计算精度
        num_right=np.sum((predictlabels==testlabels).astype('float'))
        accuracy=(num_right/num_test)*100
        print('n_components = %d: accuracy = %.2f%%'%(num_c,accuracy))
        
        size_accuracy.append(accuracy)
    
    max_id=np.argmax(size_accuracy)
    if size_accuracy[max_id]>max_acc:
        max_acc=size_accuracy[max_id]
        max_acc_n_components=num_components[max_id]
        max_acc_k=k_c
    
    #将结果可视化
    plt.figure(figsize=(12,8))
    plt.plot(num_components,size_accuracy,'r-')
    plt.plot(num_components,size_accuracy,'go')
    plt.xlabel('n_components')
    plt.ylabel('accuracy(%)')
    plt.title('k=%d'%(k_c))
    plt.show()

print('\n\nThe result:max_acc = %.2f%%, max_acc_n_components = %d,max_acc_k = %d'%(max_acc,max_acc_n_components,max_acc_k))


