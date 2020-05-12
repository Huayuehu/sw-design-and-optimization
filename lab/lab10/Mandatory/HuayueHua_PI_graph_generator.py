"""
Name: Huayue Hua
USC ID: 9817961224
"""
# Commands: python3 HuayueHua_PI_graph_generator.py

import HuayueHua_PI_tree_checker as tc
import random
import time

random.seed(time.time())

NODE_SIZE = 8


def create_graph(node_num, edge_num):
    filename = "./input.txt"
    fout = open(filename, 'w')

    if node_num == 0 and edge_num == 0:
        fout.write(str(0) + '\n')
        fout.write(str(0) + '\n')
    elif edge_num == node_num * (node_num - 1) / 2:
        fout.write(str(node_num) + '\n')
        fout.write(str(edge_num) + '\n')
        for i in range(node_num):
            for j in range(i + 1, node_num):
                fout.write(str(i) + ',' + str(j) + '\n')
    else:
        fout.write(str(node_num) + '\n')
        fout.write(str(edge_num) + '\n')
        result_list = []
        k = 0
        while k < edge_num:
            temp = [random.randint(0, node_num - 1), random.randint(0, node_num - 1)]
            temp2 = [temp[1], temp[0]]
            if temp[0] != temp[1] and temp not in result_list and temp2 not in result_list:
                result_list.append(temp)
                fout.write(str(temp[0]) + ',' + str(temp[1]) + '\n')
                k = k + 1
    fout.close()


if __name__ == '__main__':
    """
    For every case, we rewrite input.txt and call tree_checker
    case 1: 0 node, 0 edge x 1
    case 2: fully connected (with 5 nodes) x 1
    case 3: at least 5 nodes, 2 edges x 2
    case 4: other scenarios
    """
    # case 1: 0 node, 0 edge x 1
    print("------------------------- case 1: 0 node, 0 edge -------------------------")
    print("Graph 1")
    create_graph(0, 0)
    tc.main()

    # case 2: fully connected (with 5 nodes) x 1
    print("----------------- case 2: fully connected (with 5 nodes) -----------------")
    print("Graph 2")
    create_graph(5, 10)
    tc.main()

    # case 3: at least 5 nodes, 2 edges x 2
    print("----------------------- case 3: 6 nodes, 2 edges -------------------------")
    print("Graph 3")
    create_graph(6, 2)
    tc.main()

    # case 4: other scenario
    print("------------------------ case 4: other scenarios -------------------------")
    n = 4
    while n < 21:
        print("Graph ", n)
        node_num = random.randint(0, NODE_SIZE)
        max_edge = node_num * (node_num - 1) / 2
        edge_num = random.randint(0, max_edge)
        create_graph(node_num, edge_num)
        tc.main()
        n = n + 1
