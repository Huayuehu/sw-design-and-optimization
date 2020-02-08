//
// Created by Huayue Hua on 2020-02-06.
//

# include "MemberListTester.h"
# include "MemberList.h"
# include <iostream>
# include <fstream>
# include <cassert>
using namespace std;

void MemberListTester::runTests() {
    cout<<"Testing class MemberList..."<<endl;
    testConstructors();
    testSearchMember();
    cout<<"All tests passed!"<<endl;
}

void MemberListTester::testConstructors() {
    cout<<"- constructors..."<<flush;

    MemberList bList("./input.txt");
    assert( bList.getNumMembers() == 5 );
    cout << " 0 " << flush;

    cout << " Passed!" << endl;
}

void MemberListTester::testSearchMember() {
    cout << "- searchMember()...  " << flush;

    /*
     * First, test find Member via username
     */
    cout << "1. Find Member via username" << flush;
    ofstream fout1("./output.txt");
    assert(fout1.is_open());

    MemberList blist("./input.txt");
    blist.searchMember("spiderman", fout1);
    fout1.close();

    // use readFrom() to see whether searchMember() worked
    ifstream fin1("./output.txt");
    assert(fin1.is_open());
    Member Member1;
    Member1.readFrom(fin1);
    assert(Member1.getUsername() == "spiderman" );
    assert(Member1.getName() == "Jane Scott" );
    assert(Member1.getDateBirth() == "02/17/1998" );
    assert(Member1.getEmail() == "janescott@gmail.com" );
    assert(Member1.getPhoneNumber() == "2133770909"  );
    assert(Member1.getYear() == 2017);
    fin1.close();
    cout << " passed!  ";


    /*
     * Second, test find Member via email
     */
    cout << "2. Find Member via email" << flush;
    ofstream fout2("./output.txt");
    assert(fout2.is_open());
    blist.searchMembers("janescott@gmail.com", fout2);
    fout2.close();

    // use readFrom() to see whether searchMember() worked
    ifstream fin2("./output.txt");
    assert(fin2.is_open());
    Member Member2;
    Member2.readFrom(fin2);
    assert(Member2.getUsername() == "spiderman" );
    assert(Member2.getName() == "Jane Scott" );
    assert(Member2.getDateBirth() == "02/17/1998" );
    assert(Member2.getEmail() == "janescott@gmail.com" );
    assert(Member2.getPhoneNumber() == "2133770909"  );
    assert(Member2.getYear() == 2017);
    fin2.close();
    cout << " passed!  ";


    /*
     * Third, find all the Members via registered year
     */
    cout << "3. Find all Members via registered year" << flush;
    ofstream fout3("./output.txt");
    assert(fout3.is_open());
    blist.searchMembers(2017, fout3);
    fout3.close();

    // use readFrom() to see whether searchMember() worked
    ifstream fin3("./output.txt");
    assert(fin3.is_open());
    Member Member3;
    Member3.readFrom(fin3);
    assert(Member3.getUsername() == "spiderman" );
    assert(Member3.getName() == "Jane Scott" );
    assert(Member3.getDateBirth() == "02/17/1998" );
    assert(Member3.getEmail() == "janescott@gmail.com" );
    assert(Member3.getPhoneNumber() == "2133770909"  );
    assert(Member3.getYear() == 2017);

    string seperator;
    getline(fin3, seperator);
    Member3.readFrom(fin3);
    assert(Member3.getUsername() == "superman" );
    assert(Member3.getName() == "Tony Lee" );
    assert(Member3.getDateBirth() == "01/11/1996" );
    assert(Member3.getEmail() == "tony11@gmail.com" );
    assert(Member3.getPhoneNumber() == "2131237700"  );
    assert(Member3.getYear() == 2017);
    cout << " passed! "<< endl;
    fin3.close();
}