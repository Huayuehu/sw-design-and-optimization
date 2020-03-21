import matplotlib.pyplot as plt

x_values = list(range(1, 101))
y_values = [x ** 2 for x in x_values]

plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolors = 'none', s = 40)
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)
plt.tick_params(axis = 'both', labelsize = 14)
plt.axis([0, 110, 0, 11000]) // x_min, x_max, y_min, y_max
#plt.show()
plt.savefig('squares_plot.png', bbox_inches = 'tight')