import java.util.*; 
import java.lang.*; 
import java.io.*; 

class Graph 
{ 
	int V, E; // V-> no. of vertices & E->no.of edges 
	Edge edge[]; // /collection of all edges 

	class Edge { 
		int src, dest; 
	}; 

    // constructor
	Graph(int v, int e) { 
		V = v; 
		E = e; 
		edge = new Edge[E]; 
		// declare 3 empty edge pair
		for (int i = 0; i < E; i++) {
		    edge[i] = new Edge(); 
		}
	} 

	// to find the subset of an element i 
	int find(int[] parent, int i) { 
		if (parent[i] == -1) 
			return i; 
		return find(parent, parent[i]); 
	} 

	//to do union of two subsets 
	void Union(int[] parent, int x, int y) { 
		int xset = find(parent, x); 
		int yset = find(parent, y); 
		parent[xset] = yset; 
	} 


	int isCycle(Graph graph) { 
		// Allocate memory for creating V subsets 
		int parent[] = new int[graph.V]; 
        Arrays.fill(parent, -1);

		for (int i = 0; i < graph.E; i++) { 
			int x = graph.find(parent, graph.edge[i].src); 
			int y = graph.find(parent, graph.edge[i].dest); 

			if (x == y) return 1; 
			
            // x != y
			graph.Union(parent, x, y); 
		} 
		return 0; 
	} 

	public static void main (String[] args) { 
		/* 
		0 
		| \ 
		|   \ 
		1----2 */
		int V = 3, E = 3; 
		Graph graph = new Graph(V, E); 

		// add edge 0-1 
		graph.edge[0].src = 0; 
		graph.edge[0].dest = 1; 

		// add edge 1-2 
		graph.edge[1].src = 1; 
		graph.edge[1].dest = 2; 

		// add edge 0-2 
		graph.edge[2].src = 0; 
		graph.edge[2].dest = 2; 

		if (graph.isCycle(graph) == 1) {
		    System.out.println("graph contains cycle."); 
		} else {
		    System.out.println("graph doesn't contain cycle.");
		}
	} 
} 
