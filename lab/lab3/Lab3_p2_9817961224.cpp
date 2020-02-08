//
// Created by Huayue Hua on 2020-02-05.
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
    Number nums[100];
    bool check_independence(NumberSet subSet);
};

bool NumberSet::check_independence(NumberSet subSet) {
    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 100; j++) {
            if (nums[i].get_value() == subSet.nums[j].get_value()) {
                return false;
            }
        }
    }
    return true;
}

class FastNumberSet : public NumberSet {
public:
    bool check_independence(NumberSet subSet);
};

bool FastNumberSet::check_independence(NumberSet subSet) {
    list<int> table;
    for (int i = 0; i < 100; i++) {
        int key = nums[i].get_value();
        table.push_front(key);
    }

    for (int j = 0; j < 100; j++) {
        int key = subSet.nums[j].get_value();
        list<int>::iterator it;
        for (it = table.begin(); it != table.end(); it++) {
            if (*it == key) {
                return false;
            }
        }
    }
    return true;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        cout << "Please enter input file name after '" << argv[0] << "'." << endl;
        return 1;
    }

    ifstream input_file(argv[1]);
    ofstream output_file("output_hash.txt");

    if (!(input_file)) {
        cout << "Unable to open file." << endl;
    }

    FastNumberSet subSets[200];
    int value;

    for (int i = 0; i < 200; i++) {
        for (int j = 0; j < 100; j++) {
            input_file >> value;
            subSets[i].nums[j].set_value(value);
        }
    }
    input_file.close();

    for (int i = 0; i < 200; i++) {
        for (int j = i + 1; j < 200; j++) {
            if (!subSets[i].check_independence(subSets[j])) {
                output_file << "N";
                output_file.close();
                return 0;
            }
        }
    }
    output_file << "Y";
    output_file.close();
    return 0;
}

