import random
import subprocess
import math

f = open("result.txt", 'w')

def cross_entropy(Zcomputed, Zblackbox):
	print("<", end = "", file = f)
	result1 = Zcomputed * math.log(Zblackbox, 2)
	print(result1, end = "", file = f)
	print("> <", end = "", file = f)
	result2 = Zblackbox * math.log(Zcomputed, 2)
	print(result2, end = "", file = f)
	print(">", file = f)
	return

n = 10000
while(n > 0):
	a = random.uniform(-100.0, 100.0)
	x = round(a, 2)
	a = random.uniform(-100.0, 100.0)
	y = round(a, 2)
	d = random.randint(0, 100)
	Zblackbox = subprocess.check_output("./blackbox 1 2 3", shell = True)
	Zblackbox = float(Zblackbox)
	Zcomputed = math.pow(x, 2) + math.pow(y, 2)
	cross_entropy(Zcomputed, Zblackbox)
	n = n - 1
	
# # random floating point pairs (x, y)
# x = []
# y = []
# for i in range(10000):
#     a = random.uniform(-100.0, 100.0)
#     x.append(round(a, 2))
#     a = random.uniform(-100.0, 100.0)
#     y.append(round(a, 2))

# # Generate d from 0 to 100
# d = random.randint(0, 100)

# # Zblackbox
# Zblackbox = subprocess.check_output("./blackbox 1 2 3", shell = True)
# Zblackbox = float(Zblackbox)
# print(Zblackbox) 

# # Zcomputed
# for i in range(10000):
# 	Zcomputed = math.pow(x[i], 2) + math.pow(y[i], 2)
# 	# print(Zcomputed)




