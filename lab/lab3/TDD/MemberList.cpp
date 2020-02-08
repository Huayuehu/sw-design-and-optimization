//
// Created by Huayue Hua on 2020-02-06.
//
#include "MemberList.h"
#include <fstream>
#include <cassert>

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

void MemberList::searchMember(string username, ostream &out) {
    for (int i = 0; i < this->totalMembers.size(); i++) {
        if (this->totalMembers[i].getUsername() == username) {
            out << this->totalMembers[i].getUsername() << '\n'
                << this->totalMembers[i].getName() << '\n'
                << this->totalMembers[i].getDateBirth() << '\n'
                << this->totalMembers[i].getEmail() << '\n'
                << this->totalMembers[i].getPhoneNumber() << '\n'
                << this->totalMembers[i].getYear() << '\n';
        }
    }
}

void MemberList::searchMembers(string email, ostream &out) {
    for (int i = 0; i < this->totalMembers.size(); i++) {
        if (this->totalMembers[i].getEmail() == email) {
            out << this->totalMembers[i].getUsername() << '\n'
                << this->totalMembers[i].getName() << '\n'
                << this->totalMembers[i].getDateBirth() << '\n'
                << this->totalMembers[i].getEmail() << '\n'
                << this->totalMembers[i].getPhoneNumber() << '\n'
                << this->totalMembers[i].getYear() << '\n';
        }
    }
}

void MemberList::searchMembers(unsigned year, ostream &out) {
    for (int i = 0; i < this->totalMembers.size(); i++) {
        if (this->totalMembers[i].getYear() == year) {
            out << this->totalMembers[i].getUsername() << '\n'
                << this->totalMembers[i].getName() << '\n'
                << this->totalMembers[i].getDateBirth() << '\n'
                << this->totalMembers[i].getEmail() << '\n'
                << this->totalMembers[i].getPhoneNumber() << '\n'
                << this->totalMembers[i].getYear() << '\n' << '\n';
        }
    }
}