"""
Name: Huayue Hua
USC ID: 9817961224
"""
# Commands: python3 HuayueHua_PII_top_execute.py

import subprocess
import os


os.system("python3 ./HuayueHua_PI_tree_checker.py")
fin = open("./tree_output.txt", 'r')
temp = fin.readline().strip()
if temp == "tree":
	subprocess.call(["g++", "HuayueHua_PII.cpp"])
	subprocess.call(["./a.out"])
else:
	print("This graph is not a tree. Don't need further steps.")
