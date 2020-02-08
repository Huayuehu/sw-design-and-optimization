//
// Created by Huayue Hua on 2020-02-05.
//

#ifndef TEST_MEMBER_H
#define TEST_MEMBER_H

# include <iostream>
# include <string.h>
using namespace std;

class Member
{
private:
    string username;
    string name;
    string datebirth;
    string email;
    string phonenumber;
    unsigned year;
public:
    Member();
    Member(const string& username, const string& name, const string& datebirth, const string& email, const string& phonenumber, unsigned year);
    string getUsername();
    string getName();
    string getDateBirth();
    string getEmail();
    string getPhoneNumber();
    unsigned getYear();
    void readFrom(istream& in);
    void writeTo(ostream& out);
};

#endif //TEST_MEMBER_H
