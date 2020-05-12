#include <iostream>
#include <list>
#include <fstream>
#define NIL -1
using namespace std;


class Graph {
	int node_num; // No. of vertices
public:
	int edge_num;
	Graph(int node_num) {
		this->node_num = node_num;
		adj = new list<int>[node_num];
	}
	void addEdge(int v, int w) {
		adj[v].push_back(w);
		adj[w].push_back(v);
	}
	void bridge() {
		fout = ofstream("./input.txt", w)
		fout << node_num << endl;
		fout << edge_num << endl;
		
	}
};


// Driver program to test above function
int main()
{
	int count = 0;
	// Create graphs given in above diagrams
	cout << "\nBridges in first graph \n";
	Graph g1(5);
	g1.addEdge(1, 0);
	count++;
	g1.addEdge(0, 2);
	count++;
	g1.addEdge(2, 1);
	count++;
	g1.addEdge(0, 3);
	count++;
	g1.addEdge(3, 4);
	count++;
	g1.edge_num = count;
	g1.bridge();

	cout << "\nBridges in second graph \n";
	Graph g2(4);
	g2.addEdge(0, 1);
	g2.addEdge(1, 2);
	g2.addEdge(2, 3);
	g2.edge_num = 3;
	g2.bridge();

	cout << "\nBridges in third graph \n";
	Graph g3(7);
	g3.addEdge(0, 1);
	g3.addEdge(1, 2);
	g3.addEdge(2, 0);
	g3.addEdge(1, 3);
	g3.addEdge(1, 4);
	g3.addEdge(1, 6);
	g3.addEdge(3, 5);
	g3.addEdge(4, 5);
	g3.edge_num = 8
	g3.bridge();

	return 0;
}
