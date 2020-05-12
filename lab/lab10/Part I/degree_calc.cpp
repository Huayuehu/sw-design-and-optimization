// to find the max degree of a graph
// use BFS to record max

#include <iostream>
#include <list> 
#include <limits.h> 
#include <string>
using namespace std;


class Graph {
public:
	int node_num, edge_num;
	list<int> *adjacent; // to be replaced by "edges"
	int max_degree;

	Graph(int node_num) {
		this.node_num = node_num;
		adjacent = new list<int>[node_num];
	}

	void addEdge(int node1, int node2) {
		adjacent[node1].push_back(node2);
		adjacent[node2].push_back(node1);
	}
};


int main() {
	ifstream fin("./input.txt");

	if (!fin.is_open()) {
		cout << "input file fails to open." << endl;
		return 0;
	}

	string node_temp = "";
	string edge_temp = "";
	fin >> node_temp;
	fin >> edge_temp;
	int node_num = stoi(node_temp);
	int edge_num = stoi(edge_temp);
	cout << node_num << endl;
	cout << edge_num << endl;

	Graph g(node_num);

	string str[edge_num];
	string temp = "";
	int n = 0;
	for(int i = 0; i < edge_num; i++) {
		fin >> temp;
		temp = temp.strip().split(',');
		int node1 = stoi(temp[0]);
		int node2 = stoi(temp[1]);
		cout << node1 << " " << node2 << endl;
		g.addEdge(node1, node2);
	}

}