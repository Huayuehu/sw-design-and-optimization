//
// Created by Insane on 2020-02-06.
//
#include "Book.h"

using namespace std;

Book::Book() {
    this->bookName = "";
    this->bookId = 0;
    this->bookAuthor = "";
    this->yearofPub = "";
    this->price = "";
    this->status = "";
}

Book::Book(const string &bookName, unsigned bookId, const string &bookAuthor, const string &yearofPub,
           const string &price, const string &status) {
    this->bookName = bookName;
    this->bookId = bookId;
    this->bookAuthor = bookAuthor;
    this->yearofPub = yearofPub;
    this->price = price;
    this->status = status;
}

/*
 * getter for all private variables
 */
string Book::getBookName() {
    return bookName;
}

unsigned Book::getBookId() {
    return bookId;
}

string Book::getBookAuthor() {
    return bookAuthor;
}

string Book::getYearofPub() {
    return yearofPub;
}

string Book::getPrice(){
    return price;
}

string Book::getStatus() {
    return status;
}

void Book::readFrom(istream& in) {
    getline(in, this->bookName);
    string bookIdString;
    getline(in, bookIdString);
    this->bookId = atoi(bookIdString.c_str());
    getline(in, this->bookAuthor);
    getline(in, this->yearofPub);
    getline(in, this->price);
    getline(in, this->status);
}


