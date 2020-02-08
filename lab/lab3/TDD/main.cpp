// This is main.cpp for Member part

#include "MemberTester.h"
#include "MemberListTester.h"
#include <iostream>
using namespace std;

int main()
{
    MemberTester memberTester;
    memberTester.runTests();

    cout<<endl;

    MemberListTester memberListTester;
    memberListTester.runTests();

}