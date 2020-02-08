//
// Created by Insane on 2020-02-07.
//

#include <iostream>
#include <stdio.h>
#include <fstream>
#include <stdlib.h>
#include <cstdlib>
#include <list>

using namespace std;


class Number {
private:
    int value;
public:
    void set_value(int v) { value = v; }
    int get_value() { return value; }
};

class NumberSet {
public:
    Number nums[10];
    bool check_independence(NumberSet subSet);
};

//bool NumberSet::check_independence(NumberSet subSet) {
//    for (int i = 0; i < 10; i++) {
//        for (int j = 0; j < 10; j++) {
//            if (nums[i].get_value() == subSet.nums[j].get_value()) {
//                return false;
//            }
//        }
//    }
//    return true;
//}

class HashTable {
public:
    int hashtable[9000];
    int value[9000];
    HashTable();
    int hash(int x);
    HashTable add(NumberSet subSet);
    bool search(int x);
};

HashTable::HashTable() {
    for (int i = 0; i < 10; ++i) {
        hashtable[i] = 0;
        value[i] = 0;
    }
}


int HashTable::hash(int x) {
    int i1 = x % 20;
    int res = 23 - (i1 % 23);
    return res;
}

HashTable HashTable::add(NumberSet subSet) {
    cout<<"ADD"<<endl;
    HashTable h;
    for (int i = 0; i < 10; i++) {
        int x = subSet.nums[i].get_value();
        if(hashtable[hash(x)] != 0){
        }
        int index = hash(x);
        // cout<<"x: "<<x<<" index: "<<index<<endl;
        hashtable[index] = 1;
        value[index] = x;
    }
    return h;
}

// return true if x is in the hash table
bool HashTable::search(int x) {
    int index = hash(x);
    if (value[index] == x) {return true;}
    return false;
}

class FastNumberSet : public NumberSet {
public:
    bool check_independence(NumberSet subSet);
};

bool FastNumberSet::check_independence(NumberSet subSet) {
    HashTable h1, h2;
    h2 = h1.add(subSet);

    for (int i = 0; i < 10; i++) {
        cout<<"to check other subset nums["<<i<<"]."<<endl;
        bool b = h2.search(subSet.nums[i].get_value());
        if (b == true) {return false;}
    }
    return true;

}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        cout << "Please enter input file name after '" << argv[0] << "'." << endl;
        return 1;
    }

    ifstream input_file(argv[1]);
    ofstream output_file("./output_hash.txt");

    assert(input_file.is_open());
    assert(output_file.is_open());

    FastNumberSet subSets[20];
    int value;
    for (int i = 0; i < 20; i++) {
        for (int j = 0; j < 10; j++) {
            input_file >> value;
            subSets[i].nums[j].set_value(value);
        }
    }

    for (int i = 0; i < 20; i++) {
        for (int j = i + 1; j < 20; j++) {
            cout<<"subset i, subset j: "<<i<<", "<<j<<endl;
            if (!subSets[i].check_independence(subSets[j])) {
                output_file << "N";
                output_file.close();
                return 0;
            }
        }
    }
    output_file << "Y";
    input_file.close();
    output_file.close();
    return 0;
}

