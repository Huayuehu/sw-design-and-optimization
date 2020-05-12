import math


def find(parent, i):
	if parent[i] != i:
		return find(parent, parent[i])
	else:
		return i


def union(parent, rank, x, y):
	xroot = find(parent, x)
	yroot = find(parent, y)

	if rank[xroot] < rank[yroot]:
		parent[xroot] = yroot
	elif rank[xroot] > rank[yroot]:
		parent[yroot] = xroot
	else:
		parent[xroot] = yroot
		rank[yroot] += 1


def mst(edges, n):
	result = [] # to store the mst result, contains the src and dst of the edges
	parent = []
	rank = []

	# initialize parent[] and rank[]
	for i in range(n):
		parent.append(i)
		rank.append(0)

	e_index = 0 # index of result edge
	i = 0 # index of sorted edge
	sum = 0
	while e_index < n - 1 and i < len(edges) - 1:
		# get each edge and check if there is a cycle
		edge = edges[i]
		x = find(parent, edge[0])
		y = find(parent, edge[1])
		i = i + 1

		# x != y
		# put into result and do union
		if x != y:
			result.append([edge[0] + 1, edge[1] + 1])
			e_index = e_index + 1
			union(parent, rank, x, y)
		# else do nothing
	return result


if __name__ == '__main__':
	# read input.txt
	filename = "input.txt";
	coordinates = []
	with open(filename, 'r') as f:
		lines = f.readlines()
		n = int(lines[0])
		for i in range(1, n + 1):
			temp = lines[i].split(' ')
			x = int(temp[1])
			y = int(temp[2])
			coordinates.append([x, y])

	# calculate distance and store the edges and corresponding distance/weight
	edges = []
	for i in range(n - 1):
		for j in range(i + 1, n):
			delta_x = coordinates[i][0] - coordinates[j][0]
			delta_y = coordinates[i][1] - coordinates[j][1]
			sum_xy = pow(delta_x, 2) + pow(delta_y, 2)
			distance = math.sqrt(sum_xy)
			edges.append([i, j, distance])
	edges = sorted(edges, key = lambda item: item[2]);
	result = mst(edges, n)

	with open("output.txt", 'w') as f:
		f.write("The total number of edges: " + str(len(result)) + "\n")
		for re in result:
			f.write(str(re[0]) + " " + str(re[1]) + "\n")

			