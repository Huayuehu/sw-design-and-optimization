//https://www.geeksforgeeks.org/bridge-in-a-graph/
#include <iostream>
#include <fstream>
#include <sstream>
#include <list>
#include <string>
#include <vector>

using namespace std;
ofstream op("Part2_result.txt");

template <typename T>
void swap(T *x, T *y){
	T tmp = *x;
	*x = *y;
	*y = tmp;
}

void swapVec(int *x, int *y){
	int tmp = *x;
	*x = *y;
	*y = tmp;
}

class Graph{
private:
	bool hasBridge;
	int n;
	int e;
	vector<int> *graph;
	vector<int> *dirGraph;
	void DFS(int pred, bool visited[], int visitOrder[], int belongTo[], int parent[]);

public:
	Graph(int, int);
	void AddEdge(int, int);
	int get_node(){return n;}
	int get_edge(){return e;}
	void print_graph();
	void MaxDegree();
	void BridgeFinder();
	void TopoSort();

};

int main(int argc, char *argv[]) {
	ifstream ip(argv[1]);
	int node, edge;
	ip >> node;
	ip >> edge;
	vector<int> record;
	Graph g(node, edge);
	while(ip){
		string s;
		if(!getline(ip, s)) break;

		istringstream ss(s);

		while(ss){
			string s;
			if(!getline(ss, s, ',')) break;
			record.push_back(stoi(s));
		}
	}
	ip.close();

	for(int i=0; i<record.size(); i+=2){
		g.AddEdge(record[i], record[i+1]);
	}

	//g.print_graph();
	g.MaxDegree();	
	g.BridgeFinder();
	op.close();
	
	g.TopoSort();
}

Graph::Graph(int n, int e){
	this->n = n;
	this->e = e;
	graph = new vector<int>[n];
	dirGraph = new vector<int>[n];
	hasBridge = false;
}

void Graph::AddEdge(int v1, int v2){
	graph[v1].push_back(v2);
	graph[v2].push_back(v1);
	dirGraph[v1].push_back(v2);
}

void Graph::print_graph(){
	for(int i=0; i<n; i++){
		cout << i <<": ";
		for(int j=0; j<dirGraph[i].size(); j++){
			cout << dirGraph[i][j] <<" ";
		}
		cout<<endl;
	}
} 

void Graph::DFS(int pred, bool visited[], int visitOrder[], int belongTo[], int parent[]){
	static int counter = 0;
	visited[pred] = true;
	visitOrder[pred] = belongTo[pred] = ++counter;

	for (int i = 0; i < graph[pred].size(); i++){
		int succ = graph[pred][i];

		if(!visited[succ]){
			parent[succ] = pred;
			DFS(succ, visited, visitOrder, belongTo, parent);

			belongTo[pred] = min(belongTo[pred], belongTo[succ]);

			if(belongTo[succ] > visitOrder[pred]){
				if(!hasBridge){
					hasBridge = true;
					op <<"bridge exist:"<<endl;
				}
				op << pred <<" "<< succ << endl;
			}
		}

		else if(succ != parent[pred])
			belongTo[pred] = min(belongTo[pred], visitOrder[succ]);
	}
}

void Graph::BridgeFinder(){
	bool *visited = new bool[n];
	int *visitOrder = new int[n];
	int *belongTo = new int[n];
	int *parent = new int[n];

	for(int i=0; i<n; i++){
		parent[i] = -1;
		visited[i] = false;
	}

	for(int i=0; i<n; i++){
		if(visited[i] == false)
			DFS(i, visited, visitOrder, belongTo, parent);
	}

	if(!hasBridge) op <<"This graph has no bridge"<<endl;
}

void Graph::MaxDegree(){
	int maxDeg = 0;

	for(int i=0; i<n; i++)
		if(graph[i].size() > maxDeg)
			maxDeg = graph[i].size();
		
	for(int i=0; i<n; i++)
		if(graph[i].size() == maxDeg)
			op <<"Node "<< i <<" has max undirected degree of "<< maxDeg << endl;

}

void Graph::TopoSort(){
	// Topological sort based on directed degree
	int maxDirDeg;
	int topo[n];
	for(int i=0; i<n; i++)
		topo[i] = i;

	for(int i=0; i<n-1; i++){
		maxDirDeg = i;
		for(int j=i+1; j<n; j++)
			if(dirGraph[j].size() > dirGraph[maxDirDeg].size())
				maxDirDeg = j;

		swap<vector<int> >(&dirGraph[maxDirDeg], &dirGraph[i]);
		swap<int>(&topo[maxDirDeg], &topo[i]);
	}
	cout << "Topological Sort based on directed degree: ";
	for(int i=0; i<n; i++)
		cout << topo[i] <<" "; 
	cout<<endl;
	

}

