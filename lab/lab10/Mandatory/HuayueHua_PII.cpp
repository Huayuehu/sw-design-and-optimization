/**
Name: Huayue Hua
USC ID: 9817961224

To write bridge checker part, I take 
https://www.geeksforgeeks.org/bridge-in-a-graph/
as a reference

To write topo sort part, I take 
https://songlee24.github.io/2015/05/07/topological-sorting/
as a reference
*/
// Commands: python3 HuayueHua_PII_top_execute.py


#include <iostream>
#include <list>
#include <limits.h>
#include <string>
#include <fstream>
#include <sstream>
#include <queue>
using namespace std;


class Graph {
public:
    int node_num;
    list<int> *edges;  // represent all the node2 connected to node1
    int max_degree;
    bool bridge_flag;
    list<int> *directed_edges;  // store directed adjacent edges
    int *in_degree;  // store the input degree for every node in directed graph
    queue<int> q;  // to perform bfs


    Graph(int node_num) {
        this->node_num = node_num;
        edges = new list<int>[node_num];
        bridge_flag = false;
        directed_edges = new list<int>[node_num];
        in_degree = new int[node_num];
        for (int i = 0; i < node_num; i++) {
            in_degree[i] = 0;
        }
        
    }

    void addEdge(int node1, int node2) {
        edges[node1].push_back(node2);
        edges[node2].push_back(node1);
        directed_edges[node1].push_back(node2);
        in_degree[node2]++;
    }


    void dfs(int node, int time, bool visited[], int visited_time[], int less_time[], int parent[]) {
        visited[node] = true;

        visited_time[node] = time + 1;
        less_time[node] = time + 1;

        list<int>::iterator i;
        for (i = edges[node].begin(); i != edges[node].end(); i++) {
            // if not visited, then recursively visit all the edges connected
            if (!visited[*i]) {
                parent[*i] = node;
                dfs(*i, time + 1, visited, visited_time, less_time, parent);

                less_time[node] = min(less_time[node], less_time[*i]);
                if (visited_time[node] < less_time[*i]) {  // node - *i is a bridge
                    bridge_flag = true;
                    return;
                }

            }
            // if visited and the visited node is not the parent of node 
            // => there is a loop, *i is also a parent of node
            // node - *i can not be a bridge
            // to update less_time for current node
            else if (*i != parent[node]) {
                less_time[node] = min(less_time[node], visited_time[*i]);
            }
        }

    }

    void calc_degree() {
        int *result_list = new int[node_num];
        for (int i = 0; i < node_num; i++) {
            int curr_degree = edges[i].size();
            max_degree = max(max_degree, curr_degree);
            result_list[i] = -1;
        }

        for (int i = 0; i < node_num; i++) {
            if (edges[i].size() == max_degree) {
                result_list[i] = 1;
            }
        }

        cout << "The maximum degree is " << max_degree << " for node number";
        for (int i = 0; i < node_num; i++) {
            if (result_list[i] == 1) {
                cout << " " << i;
            }
        }
        cout << "." << endl;

    }

    void bridge_checker() {
        // preparation
        bool *visited = new bool[node_num];
        int *visited_time = new int[node_num];  // stores the discovery time of the visied node
        int *less_time = new int[node_num];  // stores the less time that the node be visited if exists
        int *parent = new int[node_num];

        for (int i = 0; i < node_num; i++) {
            visited[i] = false;
            parent[i] = -1;
        }


        for (int i = 0; i < node_num; i++) {
            if (!visited[i]) {
                dfs(i, 0, visited, visited_time, less_time, parent);
            }
        }

        if (bridge_flag) {
            cout << "There is at least one bridge in this graph." << endl;
        } else {  // if return with no bridge, print out corresponding info
            cout << "There is no bridge in this graph." << endl;
        }
    }

    void topological_sort() {
        for (int i = 0; i < node_num; i++) {
            if (in_degree[i] == 0) {  // root node
                q.push(i);
            }
        }

        cout << "After topological sort: ";
        while(!q.empty()) {
            int curr = q.front();
            q.pop();
            cout << curr << " ";
            
            list<int>::iterator i;
            for (i = directed_edges[curr].begin(); i != directed_edges[curr].end(); i++) {
                in_degree[*i]--;
                if (in_degree[*i] == 0) {
                    q.push(*i);
                }
            }
        }
    }
};


int main() {
    ifstream fin("input.txt");

    if (!fin.is_open()) {
        cout << "input file fails to open." << endl;
        return 0;
    }

    string node_temp;
    string edge_temp;
    fin >> node_temp;
    fin >> edge_temp;
    int node_num = stoi(node_temp);
    int edge_num = stoi(edge_temp);
    // cout << node_num << endl;
    // cout << edge_num << endl;

    Graph g(node_num);
    string str[edge_num];
    string temp;
    int n = 0;
    for (int i = 0; i < edge_num; i++) {
        fin >> temp;
//        cout << temp << endl;

        char *s_input = (char *)temp.c_str();
        const char * split = ",";
        char *p = strtok(s_input, split);
        int node1, node2;
        node1 = atoi(p);  // char * -> int
        p = strtok(NULL, split);
        node2 = atoi(p);

        // cout << node1 << " " << node2 << endl;
        g.addEdge(node1, node2);
    }

    g.calc_degree();
    g.bridge_checker();
    g.topological_sort();
    cout << endl;


}