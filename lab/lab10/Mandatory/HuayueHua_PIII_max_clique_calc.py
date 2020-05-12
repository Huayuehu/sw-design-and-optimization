"""
Name: Huayue Hua
USC ID: 9817961224
"""
# Commands: python3 HuayueHua_PIII_clique_checker.py


from collections import defaultdict


def is_clique(nodes_list, graph):
	temp = []

	for i in nodes_list:
		for j in nodes_list:
			if (j != i):
				if j not in graph[i]:
					return False
	return True


def max_clique(node1, node2, nodes_list, graph):
	max_clique_size = 0
	if node1 not in nodes_list:
		nodes_list.append(node1)
	if node2 not in nodes_list:
		nodes_list.append(node2)

	for i in graph[node2]:
		if i not in nodes_list:
			nodes_list.append(i)
			if is_clique(nodes_list, graph):
				max_clique(node2, i, nodes_list, graph)
				max_clique_size = max(max_clique_size, len(nodes_list))
			else:
				nodes_list.remove(i)
	return max_clique_size


def main():
	# read input.txt
	fin = open("./input.txt", 'r')
	lines = fin.readlines()
	nodes = lines[0].split()
	edges = lines[1].split()
	node_num = int(nodes[0])
	edge_num = int(edges[0])
	graph = defaultdict(list)
	if node_num == 0 and edge_num == 0:
		print("No clique found.")
		fin.close()
		return
	else:
		for i in range(2, edge_num + 2):
			temp = lines[i].strip().split(',')
			node1 = int(temp[0])
			node2 = int(temp[1])
			graph[node1].append(node2)
			graph[node2].append(node1)
	fin.close()

	nodes_list = []
	max_clique_size = max_clique(0, 1, nodes_list, graph)
	if (max_clique_size > 0):
		print("Clique number (%d): " % max_clique_size, end="")
		for i in nodes_list:
			print(str(i) + ' ', end='')
		print('')
	else:
		print("No clique found.")


if __name__ == '__main__':
	main()