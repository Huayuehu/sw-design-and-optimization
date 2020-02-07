//
// Created by Insane on 2020-02-06.
//
#include "MemberList.h"
#include <fstream>

/*
 * MemberList constructor
 * @param: fileName, a string
 * Precondition: fileName contains the name of a input file.
 */
MemberList::MemberList(const string& fileName) {
    // open a stream to the Memberlist file
    ifstream fin( fileName.c_str() );
    assert( fin.is_open() );

    // read each Member and append it to totalMembers
    Member Member;
    string separator;
    while (true) {
        Member.readFrom(fin);
        if ( !fin ) { break; }
        getline(fin, separator);
        totalMembers.push_back(Member);
    }
    // close the stream
    fin.close();
}



/*
 * Retrieve length of the Member list
 * Return: the number of Members in the list.
 */

unsigned MemberList::getNumMembers() const {
    return totalMembers.size();
}
