#include <iostream>
#include <stdio.h>
#include <fstream>
#include <stdlib.h>
using namespace std;

class Number {
private:
    int value;
public:
    void set_value(int v) {value = v;}
    int get_value() {return value;}
};

class NumberSet {
public:
    Number nums[10];
    bool check_independence(NumberSet subSet);
};

bool NumberSet::check_independence (NumberSet subSet) {
    for(int i = 0; i < 10; i++) {
        for(int j = 0; j < 10; j++) {
            if(nums[i].get_value() == subSet.nums[j].get_value()) {
                return false;
            }
        }
    }
    return true;
}

int main(int argc, char *argv[]) {
    if(argc != 2) {
        cout << "Please enter input file name after '" << argv[0] << "'."<<endl;
        return 1;
    }

    ifstream input_file (argv[1]);
    ofstream output_file("output.txt");

    if(!(input_file)) {
        cout<<"Unable to open file."<<endl;
    }

    NumberSet subSets[20];
    int value;

    for(int i = 0; i < 20; i++) {
        for(int j = 0; j < 10; j++) {
            input_file>>value;
            subSets[i].nums[j].set_value(value);
        }
    }
    input_file.close();


    for(int i = 0; i < 20; i++) {
        for(int j = i + 1; j < 20; j++) {
            if(!subSets[i].check_independence(subSets[j])) {
                output_file<<"N";
                output_file.close();
                return 0;
            }
        }
    }
    output_file<<"Y";
    output_file.close();
    return 0;
}
