# -*- coding: utf-8 -*-

"""
加不加过拟合检测都能跑，以这个作为范本来修改
"""

from torchvision import datasets
import torchvision.transforms as transforms
import torch
import numpy as np
import matplotlib.pyplot as plt


def load_mnist():
	#下载数据
	train_data = datasets.MNIST(root = './data',train = True,download = True,transform = transforms.ToTensor())
	test_data = datasets.MNIST(root = './data',train = True,download = True,transform = transforms.ToTensor())

	#创建加载器
	train_loader = torch.utils.data.DataLoader(train_data,batch_size = 64,num_workers = 0)
	test_loader = torch.utils.data.DataLoader(test_data,batch_size = 64,num_workers = 0)

	return train_loader, test_loader

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

# Train the net
def train(model, epoch, train_loader, criterion, optimizer):
	model.train()
	for idx, (data, target) in enumerate(train_loader):
		optimizer.zero_grad()
		output = model(data)
		loss = F.nll_loss(output, target)
		loss.backward()
		optimizer.step()
		if idx % 50 == 49:
			print('Train epoch: %d   Loss: %.3f    ' % (epoch+1, loss))


def test(model, test_loader):
	model.eval()
	test_loss = 0.0
	class_correct = list(0. for i in range(10))
	class_total = list(0. for i in range(10))
	for data, target in test_loader:
	    output = model(data)
	    loss = criterion(output, target)
	    test_loss += loss.item()*data.size(0)
	    _, pred = torch.max(output, 1)
	    correct = np.squeeze(pred.eq(target.data.view_as(pred)))
	    for i in range(64):
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
	        print('Test Accuracy of %5s: ' % (classes[i]))

	print('\nTest Accuracy (Overall): %2d%% (%2d/%2d)' % (100. * np.sum(class_correct) / np.sum(class_total),np.sum(class_correct), np.sum(class_total)))

if __name__ == '__main__':
	train_loader, test_loader = load_mnist()

	model = Net()

	#定义损失函数和优化器
	criterion = nn.CrossEntropyLoss()
	optimizer = torch.optim.SGD(params = model.parameters(),lr = 0.01)
	epochs = 5

	for epoch in range(epochs):
		train(model, epoch, train_loader, criterion, optimizer)
		test(model, test_loader)

