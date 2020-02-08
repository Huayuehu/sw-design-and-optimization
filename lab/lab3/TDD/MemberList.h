//
// Created by Huayue Hua on 2020-02-06.
//

#ifndef TEST_MEMBERLIST_H
#define TEST_MEMBERLIST_H

#include "Member.h"
#include <string>
#include <vector>
using namespace std;

class MemberList {
private:
    vector<Member> totalMembers;
public:
    MemberList(const string& fileName);
    unsigned getNumMembers() const;
    void searchMember(string username, ostream &out);
    void searchMembers(string email, ostream &out);
    void searchMembers(unsigned year, ostream &out);
};

#endif //TEST_MEMBERLIST_H
