"""
This version detect whether the graph based on input.txt is a tree
Next step, I will implement generator and combined with checker
"""

from collections import defaultdict


def cycle_checker(node, parent, visited, loop_node):
    visited[node] = True
    loop_node.append(node)
    for i in graph[node]:  # to check all the nodes linked with this node
        if not visited[i]:  # if not visited yet, perform DFS
            if cycle_checker(i, node, visited, loop_node):
                return True  # detect cycle => return True
        elif i != parent:  # node i is visited and node i is not the parent node => cycle detected
            loop_node.append(i)
            print("This graph is not a tree. A loop in this graph:", end=" ")
            for i in loop_node:
                print(i, end=" ")
            return True

    return False  # no cycle


def connectivity_checker():
    visited = [False] * node_num

    for node in range(node_num):
        for i in graph[node]:
            visited[i] = True

    for i in range(node_num):
        if not visited[i]:
            print("This graph is not a tree. The node", i, "is not in connected to the rest of graph.")
            return False

    return True


if __name__ == '__main__':
    # read input.txt
    filename = "/Users/insane/Desktop/USC/20spring/595/lab/lab10/Part I/input.txt"
    graph = defaultdict(list)
    with open(filename, 'r') as f:
        lines = f.readlines()
        nodes = lines[0].split()
        edges = lines[1].split()
        node_num = int(nodes[0])
        edge_num = int(edges[0])
        for i in range(2, node_num + 1):
            temp = lines[i].split(',')
            node1 = int(temp[0])
            node2 = int(temp[1])
            graph[node1].append(node2)
            graph[node2].append(node1)
    # print(graph)

    # check if has cycle
    # if contains cycle, print info in cycle function and do nothing in main
    # else if no cycle, check the connectivity
    visited = [False] * node_num
    loop_node = []
    if not cycle_checker(0, -1, visited, loop_node):
        # some node didn't connect to the graph, print info in connectivity function and do nothing in main
        # all connected => is a tree, print out "This graph is a tree, i.e., it does not have a loop."
        if connectivity_checker():
            print("This graph is a tree, i.e., it does not have a loop.")
