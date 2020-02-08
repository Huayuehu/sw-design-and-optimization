//
// Created by Huayue Hua on 2020-02-05.
//

# include "MemberTester.h"
# include "Member.h"
# include <iostream>
# include <fstream>
# include <cassert>
using namespace std;

void MemberTester::runTests() {
    cout<<"Testing class Member..."<<endl;
    testConstructors();
    testReadFrom();
    testWriteTo();
    cout<<"All tests passed!"<<endl;
}

void MemberTester::testConstructors () {
    cout<<"- constructors..."<<flush;

    // default contructor
    Member member;
    assert(member.getUsername() == "");
    assert(member.getName() == "");
    assert(member.getDateBirth() == "");
    assert(member.getEmail() == "");
    assert(member.getPhoneNumber() == "");
    assert(member.getYear() == 0);
    cout<<" 0 "<<flush;

    // expilict-value constructor
    Member member2("Huayue Hua", "hhy", "11/10/1995", "huayuehu@usc.edu", "2134773485", 1995);
    assert(member2.getUsername() == "Huayue Hua");
    assert(member2.getName() == "hhy");
    assert(member2.getDateBirth() == "11/10/1995");
    assert(member2.getEmail() == "huayuehu@usc.edu");
    assert(member2.getPhoneNumber() == "2134773485");
    assert(member2.getYear() == 1995);
    cout<<" 1 "<<flush;

    cout<<" Passed!"<<endl;
}

void MemberTester::testReadFrom() {
    cout<<"- ReadFrom()..."<<flush;

    ifstream fin("./input.txt");
    assert(fin.is_open());
    Member member;

    // read first Member in input file
    member.readFrom(fin);
    assert( member.getUsername() == "spiderman" );
    assert( member.getName() == "Jane Scott" );
    assert( member.getDateBirth() == "02/17/1998" );
    assert( member.getEmail() == "janescott@gmail.com" );
    assert( member.getPhoneNumber() == "2133770909"  );
    assert( member.getYear() == 2017);
    cout << " 0 " << flush;

    // read second Member in input file
    string separator;
    getline(fin, separator);
    member.readFrom(fin);
    assert( member.getUsername() == "superman" );
    assert( member.getName() == "Tony Lee" );
    assert( member.getDateBirth() == "01/11/1996" );
    assert( member.getEmail() == "tony11@gmail.com" );
    assert( member.getPhoneNumber() == "2131237700"  );
    assert( member.getYear() == 2017);
    cout << " 1 " << flush;

    // read third Member in input file
    getline(fin, separator);
    member.readFrom(fin);
    assert( member.getUsername() == "clubusername" );
    assert( member.getName() == "Alice Flores" );
    assert( member.getDateBirth() == "05/22/1990" );
    assert( member.getEmail() == "alice1990@gmail.com" );
    assert( member.getPhoneNumber() == "2133306677"  );
    assert( member.getYear() == 2016);
    cout << " 2 " << flush;

    fin.close();
    cout<<"Passed!"<<endl;
}

void MemberTester::testWriteTo() {
    cout<<"- WriteTo()..."<<flush;
    Member member1("spiderman", "Jane Scott", "02/17/1998", "janescott@gmail.com", "2133770909", 2017);
    Member member2("superman", "Tony Lee", "01/11/1996", "tony11@gmail.com", "2131237700", 2017);
    Member member3("clubusername", "Alice Flores", "05/22/1990", "alice1990@gmail.com", "2133306677", 2016);

    // write the three Members to an output file
    ofstream fout("./output.txt");
    assert(fout.is_open());
    member1.writeTo(fout);
    member2.writeTo(fout);
    member3.writeTo(fout);
    fout.close();

    // use readFrom() to see if writeTo() worked
    ifstream fin("./output.txt");
    assert(fin.is_open());
    Member member4, member5, member6;

    // read and check the first Member
    member4.readFrom(fin);
    assert( member4.getUsername() == "spiderman" );
    assert( member4.getName() == "Jane Scott" );
    assert( member4.getDateBirth() == "02/17/1998" );
    assert( member4.getEmail() == "janescott@gmail.com" );
    assert( member4.getPhoneNumber() == "2133770909"  );
    assert( member4.getYear() == 2017);
    cout<<" 0 "<<flush;

    member5.readFrom(fin);
    assert( member5.getUsername() == "superman" );
    assert( member5.getName() == "Tony Lee" );
    assert( member5.getDateBirth() == "01/11/1996" );
    assert( member5.getEmail() == "tony11@gmail.com" );
    assert( member5.getPhoneNumber() == "2131237700"  );
    assert( member5.getYear() == 2017);
    cout << " 1 " << flush;

    member6.readFrom(fin);
    assert( member6.getUsername() == "clubusername" );
    assert( member6.getName() == "Alice Flores" );
    assert( member6.getDateBirth() == "05/22/1990" );
    assert( member6.getEmail() == "alice1990@gmail.com" );
    assert( member6.getPhoneNumber() == "2133306677"  );
    assert( member6.getYear() == 2016);
    cout << " 2 " << flush;

    fin.close();
    cout<<" Passed!"<<endl;
}