# reference: https://blog.csdn.net/qq_34364995/article/details/80518182

a = [6, 14, 19, 24, 6, 7, 6, 24, 1, 3]

outputlist = {}
for i in a:
    if i not in outputlist.keys():
        outputlist[i] = 1
    elif i in outputlist.keys():
        outputlist[i] += 1

for i in outputlist.keys():
    if outputlist[i] == 1:
        print(i)