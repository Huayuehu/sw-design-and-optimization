import random
import string
from libsvm import svm
from libsvm import svmutil

num = 1
f = open("Dataset.txt","w")
while num <= 5000:
	x = random.randint(0,100)
	y = random.randint(0,100)
	if x < 50 and y > 50:
		f.write(str(x) + " " + str(y) + ",0 \n")
		num = num + 1
	elif x > 50 and y < 50:
		f.write(str(x) + " " + str(y) + ",1 \n")	
		num = num + 1
f.close()