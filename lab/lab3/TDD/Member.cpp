//
// Created by Huayue Hua on 2020-02-05.
//

# include "Member.h"
using namespace std;

/*
 * default constructor
 */
Member::Member() {
    username = "";
    name = "";
    datebirth = "";
    email = "";
    phonenumber = "";
    year = 0;
}

/*
 * Explicit constructor
 * @param: username, a string
 * @param: name, a string
 * @param: datebirth, a string
 * @param: email, a string
 * @param: phonenumber, a string.
 * @param: year, an unsigned int.
 * Postcondition: this -> username == username &&
 *                this -> name == name &&
 *                this -> datebirth == datebirth &&
 *                this -> email == email &&
 *                this -> phonenumber == phonenumber &&
 *                this -> year == year.
 */
Member::Member(const string& username, const string& name, const string& datebirth, const string& email, const string& phonenumber, unsigned year) {
    this->username = username;
    this->name = name;
    this->datebirth = datebirth;
    this->email = email;
    this->phonenumber = phonenumber;
    this->year = year;
}

/*
 * getter for all private variables
 */
string Member::getUsername() {
    return username;
}

string Member::getName() {
    return name;
}

string Member::getDateBirth() {
    return datebirth;
}

string Member::getEmail() {
    return email;
}

string Member::getPhoneNumber() {
    return phonenumber;
}

unsigned Member::getYear() {
    return year;
}

/*
 * Member input method...
 * @param: in, an istream
 * Precondition: in contains the username, name, datebirth, email, phonenumber and registered year data for a Member.
 * Postcondition: the username, name, datebirth, email, phonenumber and registered year data have been read from in &&
 *                this -> username == username &&
 *                this -> name == name &&
 *                this -> datebirth == datebirth &&
 *                this -> email == email &&
 *                this -> phonenumber == phonenumber &&
 *                this -> year == year.
 */
void Member::readFrom(istream& in) {
    getline(in, this -> username);
    getline(in, this -> name);
    getline(in, this -> datebirth);
    getline(in, this -> email);
    getline(in, this -> phonenumber);
    string yearString;
    getline(in, yearString);
    this -> year = atoi(yearString.c_str());
}

/*
 * Member output...
 * @param: out, an ostream
 * Postcondition: out contains username, a newline,
 *                             name, a newline,
 *                             datebirth, a newline,
 *                             email, a newline,
 *                             phonenumber, a newline,
 *                             year, a newline.
 */
void Member::writeTo(ostream& out) {
    out << this -> username << '\n'
        << this -> name << '\n'
        << this -> datebirth << '\n'
        << this -> email << '\n'
        << this -> phonenumber  << '\n'
        << this -> year  << '\n';

}