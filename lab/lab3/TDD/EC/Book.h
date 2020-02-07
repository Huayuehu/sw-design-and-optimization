//
// Created by Huayue Hua on 2020-02-06.
//

#ifndef EC_BOOK_H
#define EC_BOOK_H

#include <string.h>
#include <iostream>
using namespace std;

class Book {
private:
    string bookName;
    unsigned bookId;
    string bookAuthor;
    string yearofPub;
    string price;
    string status;
public:
    Book();

    Book(const string &bookName, unsigned bookId, const string &bookAuthor, const string &yearofPub,
         const string &price, const string &status);

    string getBookName();

    unsigned getBookId();

    string getBookAuthor();

    string getYearofPub();

    string getPrice();

    string getStatus();

    void readFrom(istream& in);
};

#endif //EC_BOOK_H
