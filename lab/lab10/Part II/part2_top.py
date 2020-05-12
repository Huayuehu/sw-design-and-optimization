import subprocess
import os

# def fun():
#     os.system('python3 p1final.py')
# fun()
# print ("------------------------------------")
# subprocess.call(["g++", "p2final.cpp"])
# tmp=subprocess.call("./a.out")


os.system("python3 ./part1_tree_checker.py")
fin = open("./tree_output.txt", 'r')
temp = fin.readline().strip()
if temp == "tree":
	subprocess.call(["g++", "main.cpp"])
	subprocess.call(["./a.out"])
else:
	print("This graph is not a tree. Don't need further steps.")
