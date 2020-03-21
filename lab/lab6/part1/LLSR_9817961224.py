import numpy as np
import matplotlib.pyplot as plt

# open file and write data into population[], profit[]
filename = 'candyshop_data.txt'
population, profit, ones = [], [], []
n = 0
with open(filename, 'r') as f:
	lines = f.readlines()
	for line in lines:
		temp = line.split(',')
		population.append(float(temp[0]))
		profit.append(float(temp[1]))
		ones.append(1)
		n = n + 1 

population = np.array(population).reshape(n,1)
Y = np.array(profit).reshape(n,1)
ones = np.array(ones).reshape(n,1)

# build new X matrix
X = np.hstack((ones,population))
pseudoinverseX = np.linalg.pinv(X)
w = np.matrix(np.dot(pseudoinverseX, Y))
print("Parameter w: ", w)

newData2 = (float(w[0]) + float(w[1]) * 2) * 10000
newData5 = (float(w[0]) + float(w[1]) * 5) * 10000
print("The expected profits in the cities of 20,000 population is $", newData2)
print("The expected profits in the cities of 50,000 population is $", newData5)

plt.scatter(population, profit)
plt.title("Candy Shop Data", fontsize = 16)
plt.xlabel("Population", fontsize = 12)
plt.ylabel("Profit", fontsize = 12)
plt.tick_params(axis = 'both', labelsize = 12)
x = np.linspace(0,25,1000)
y = float(w[0]) + float(w[1]) * x
plt.plot(x,y)
plt.show()
