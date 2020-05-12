import random
from svmutil import *
i = 0
f = open(r'随机数.txt','w+')

while i < 10:
    y = int(random.random()*100)
    print(y)
    
    f.write(str(y)+"\n")
    f.flush()
    i = i + 1

li = []
with open('随机数.txt','r') as op:
    for line in op:
        lin = int(line)
        li.append(line.strip())
print(li)

lis =  sorted(li)
print(lis)

i = 0
f = open(r'E:\Python\随机数1.txt','w+')
while i < 10:
    m = li[i]
    f.write(str(m)+"\n")
    f.flush()
    i = i + 1