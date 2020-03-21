import matplotlib.pyplot as plt

filename = 'candyshop_data.txt'
population, profit = [], []

with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        temp = line.split(',')
        population.append(float(temp[0]))
        profit.append(float(temp[1]))


plt.scatter(population, profit, c = profit, cmap = plt.cm.Blues, edgecolors = 'none', s = 40)
plt.title("Candy Shop Data", fontsize = 20)
plt.xlabel("Population", fontsize = 14)
plt.ylabel("Profit", fontsize = 14)
plt.tick_params(axis = 'both', labelsize = 14)
plt.axis([0, 25, 0, 25])
plt.show()