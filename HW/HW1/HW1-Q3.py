# reference : https://blog.csdn.net/dsx1134500455/article/details/89249539

list = ['hello', 'world', 'ni', 'hao']
s = 'world'

if (s in list):
    print('The index of String s is', list.index(s))
else:
    print("String was not found. ")