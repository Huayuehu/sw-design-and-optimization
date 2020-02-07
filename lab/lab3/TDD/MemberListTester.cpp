//
// Created by Insane on 2020-02-06.
//

# include "MemberListTester.h"
# include "MemberList.h"
# include <iostream>
# include <fstream>
using namespace std;

void MemberListTester::runTests() {
    cout<<"Testing class Member..."<<endl;
    testConstructors();
    cout<<"All tests passed!"<<endl;
}

void MemberListTester::testConstructors() {
    cout<<"- constructors..."<<flush;

    MemberList bList("/Users/insane/CLionProjects/test/input.txt");
    assert( bList.getNumMembers() == 5 );
    cout << " 0 " << flush;

    cout << " Passed!" << endl;
}