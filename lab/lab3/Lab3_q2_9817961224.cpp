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

class FastNumberSet: public NumberSet{
public:
    FastNumberSet(int x): NumberSet(x){}
    int check_independence(Number*, int);
};