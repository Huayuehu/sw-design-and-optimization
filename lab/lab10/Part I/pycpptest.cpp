#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<string>
#include<vector>
#include<list>
#include<stack>

using namespace std;

#include <iostream>
#include <string>
#include <vector>
#include <sstream>


void excute(){
	// excute python part
	string python_script = "tree_checker.py ";
	string cmd = "python3 " + python_script;
	const char* command = cmd.c_str();
	// cout<<"command executed : "<< command << endl;
	system(command);
	// cout << "Finished!" << endl;
}


int main() {
	// read from orginal_input.txt
	ifstream fin("original_input.txt");
	if (!fin.is_open()) {
		cout << "input file fails to open." << endl;
		return 0;
	}
	int node_num = 0;
	int edge_num = 0;
	fin >> node_num;
	fin >> edge_num;
	string str[edge_num];
	int n = 0;
	while (n < edge_num) {
		fin >> str[n++];
	}
	
	for (int k = 0; k < edge_num; k++) {
		ofstream fout("input1.txt");
		fout << node_num << endl;
		fout << edge_num - 1 << endl;
		string temp = "";
		for (int i = 0; i < edge_num; i++) {
			// skip ith edge
			if (i != k) {
				temp = str[i];
				fout << temp << endl;
			}
		}
		excute();
		ifstream fin2("output.txt");
		int flag = -1;
		fin2 >> flag;
		if (flag == 0) {
			cout << str[k] << " is a bridge." << endl;
		}
		fout.close();
	}

	// output to input.txt
	cout << "Finished!" << endl;

	return 0;
}
