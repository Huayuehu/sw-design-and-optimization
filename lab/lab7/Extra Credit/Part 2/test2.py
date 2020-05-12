# -*- coding: utf-8 -*-

"""
加不加过拟合检测都能跑，以这个作为范本来修改
"""

from torchvision import datasets
import torchvision.transforms as transforms
import torch
import numpy as np
import matplotlib.pyplot as plt


# #非并行加载就填0
# num_workers = 0
# #决定每次读取多少图片
# batch_size = 20

# #转换成张量
# transform = transforms.ToTensor()


# #下载数据
# train_data = datasets.MNIST(root = './drive/data',train = True,download = True,transform = transform)
# test_data = datasets.MNIST(root = './drive/data',train = True,download = True,transform = transform)

# #创建加载器
# train_loader = torch.utils.data.DataLoader(train_data,batch_size = batch_size,num_workers = num_workers)
# test_loader = torch.utils.data.DataLoader(test_data,batch_size = batch_size,num_workers = num_workers)


#拆分数据集
from torch.utils.data.sampler import SubsetRandomSampler
num_workers = 0
batch_size = 20
#添加验证集，让模型自动判断是否过拟合
valid_size = 0.2

transform = transforms.ToTensor()

train_data = datasets.MNIST(root = './drive/data',train = True,download = True,transform = transform)
test_data = datasets.MNIST(root = './drive/data',train = True,download = True,transform = transform)

num_train = len(train_data)
indices = list(range(num_train))
np.random.shuffle(indices)
split = int(np.floor(valid_size * num_train))
train_idx,valid_idx = indices[split:],indices[:split]

train_sampler = SubsetRandomSampler(train_idx)
valid_sampler = SubsetRandomSampler(valid_idx)

train_loader = torch.utils.data.DataLoader(train_data,batch_size = batch_size,sampler = train_sampler,num_workers = num_workers)
valid_loader = torch.utils.data.DataLoader(train_data,batch_size = batch_size,sampler = valid_sampler)
test_loader = torch.utils.data.DataLoader(test_data,batch_size = batch_size,num_workers = num_workers)




# #可视化
# dataiter = iter(train_loader)
# images,labels = next(dataiter)
# images = images.numpy()

# fig = plt.figure(figsize = (25,4))
# for idx in np.arange(20):#前面是读20张，所以这里就是20
# 	ax = fig.add_subplot(2,20/2,idx + 1,xticks = [],yticks = [])
# 	ax.imshow(np.squeeze(images[idx]),cmap = 'gray')
  
# 	ax.set_title(str(labels[idx].item()))
# plt.show()

import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
	def __init__(self):
		super(Net,self).__init__()
		hidden_1 = 392
		hidden_2 = 392
		self.fc1 = nn.Linear(784,hidden_1)
		self.fc2 = nn.Linear(hidden_1,hidden_2)
		self.fc3 = nn.Linear(hidden_2,10)
		#使用dropout防止过拟合
		self.dropout = nn.Dropout(0.2)
		
	def forward(self,x):
		x = x.view(-1, 784)
		x = F.relu(self.fc1(x))
		x = self.dropout(x)
		x = F.relu(self.fc2(x))
		x = self.dropout(x)
		x = self.fc3(x)
		return x

  
model = Net()
#打印出来看是否正确
# print(model)

#定义损失函数和优化器

# criterion = nn.NLLLoss()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(params = model.parameters(),lr = 0.01)


n_epochs = 5

valid_loss_min = np.Inf

for epoch in range(n_epochs):
	train_loss = 0.0
	valid_loss = 0.0
  
	for data,target in train_loader:
		optimizer.zero_grad()
		output = model(data)#得到预测值

		loss = criterion(output,target)
		loss.backward()

		optimizer.step()
		train_loss += loss.item()*data.size(0)
  
  #计算检验集的损失，这里不需要反向传播
	for data,target in valid_loader:
		output = model(data)
		loss = criterion(output,target)
		valid_loss += loss.item() * data.size(0)
  
	train_loss = train_loss / len(train_loader.dataset)
	valid_loss = valid_loss / len(valid_loader.dataset)
	# print('Epoch:  {}  \tTraining Loss: {:.6f} \tValidation Loss: {:.6f}'.format(epoch + 1,train_loss,valid_loss))
	if valid_loss <= valid_loss_min:#保存模型
		# print('Validation loss decreased ({:.6f} --> {:.6f}). Saving model...'.format(valid_loss_min,valid_loss))torch.save(model.state_dict(),'model.pt')
		valid_loss_min = valid_loss


model.eval() # prep model for *evaluation*


# initialize lists to monitor test loss and accuracy
test_loss = 0.0
class_correct = list(0. for i in range(10))
class_total = list(0. for i in range(10))



for data, target in test_loader:
    # forward pass: compute predicted outputs by passing inputs to the model
    output = model(data)
    # calculate the loss
    loss = criterion(output, target)
    # update test loss 
    test_loss += loss.item()*data.size(0)
    # convert output probabilities to predicted class
    _, pred = torch.max(output, 1)
    # compare predictions to true label
    correct = np.squeeze(pred.eq(target.data.view_as(pred)))
    # calculate test accuracy for each object class
    for i in range(batch_size):
        label = target.data[i]
        class_correct[label] += correct[i].item()
        class_total[label] += 1

# calculate and print avg test loss
test_loss = test_loss/len(test_loader.dataset)
print('Test Loss: {:.6f}\n'.format(test_loss))

for i in range(10):
    if class_total[i] > 0:
        print('Test Accuracy of %5s: %2d%% (%2d/%2d)' % (
            str(i), 100 * class_correct[i] / class_total[i],
            np.sum(class_correct[i]), np.sum(class_total[i])))
    else:
        print('Test Accuracy of %5s: N/A (no training examples)' % (classes[i]))

print('\nTest Accuracy (Overall): %2d%% (%2d/%2d)' % (
    100. * np.sum(class_correct) / np.sum(class_total),
    np.sum(class_correct), np.sum(class_total)))



