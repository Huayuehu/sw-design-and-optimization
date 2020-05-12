"""
Name: Huayue Hua
USC ID: 9817961224
Reference: https://www.geeksforgeeks.org/check-given-graph-tree/
"""

from collections import defaultdict


def cycle_checker(graph, node_num, node, parent, visited, loop_node):
    visited[node] = True
    loop_node.append(node)
    for i in graph[node]:  # to check all the nodes linked with this node
        if not visited[i]:  # if not visited yet, perform DFS
            if cycle_checker(graph, node_num, i, node, visited, loop_node):
                return True  # detect cycle => return True
        elif i != parent:  # node i is visited and node i is not the parent node => cycle detected
            loop_node.append(i)
            print("This graph is not a tree. A loop in this graph:", end=" ")
            for i in loop_node:
                print(i, end=" ")
            print('') # to change line
            return True

    return False  # no cycle


def connectivity_checker(graph, node_num):
    visited = [False] * node_num

    for node in range(node_num):
        for i in graph[node]:
            visited[i] = True

    for i in range(node_num):
        if not visited[i]:
            print("This graph is not a tree. Node", i, "is not in connected to the rest of graph.")
            return False

    return True


def tree_checker():
    # read input.txt
    filename = "/Users/insane/Desktop/USC/20spring/595/lab/lab10/Part I/input.txt"
    fin = open(filename, 'r')
    lines = fin.readlines()
    nodes = lines[0].split()
    edges = lines[1].split()
    node_num = int(nodes[0])
    edge_num = int(edges[0])
    graph = defaultdict(list)
    if node_num == 0 and edge_num == 0:
        print("This graph is not a tree. There is no node and edge.")
        fin.close()
        return
    else:
        for i in range(2, edge_num + 2):
            temp = lines[i].split(',')
            node1 = int(temp[0])
            node2 = int(temp[1])
            graph[node1].append(node2)
            graph[node2].append(node1)
    fin.close()
    # print(graph)

    # check if has cycle
    # if contains cycle, print info in cycle function and do nothing in main
    # else if no cycle, check the connectivity
    visited = [False] * node_num
    loop_node = []
    if not cycle_checker(graph, node_num, 0, -1, visited, loop_node):
        # some node didn't connect to the graph, print info in connectivity function and do nothing in main
        # all connected => is a tree, print out "This graph is a tree, i.e., it does not have a loop."
        if connectivity_checker(graph, node_num, ):
            print("This graph is a tree, i.e., it does not have a loop.")


