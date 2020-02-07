//
// Created by Huayue Hua on 2020-02-06.
//

#include "BookList.h"
#include <fstream>
#include <vector>
#include <cassert>

BookList::BookList(const string &fileName) {
    // open a stream to store the BookList file
    ifstream fin (fileName.c_str());
    assert(fin.is_open());

    // read each book and append it to allBooks
    Book book;
    string separator;
    while (true) {
        book.readFrom(fin);
        if (!fin) {break;}
        getline(fin, separator);
        allBooks.push_back(book);
    }
    fin.close();
}

void BookList::findBook(string bookName, ostream &out) {
    for (int i = 0; i < this->allBooks.size(); i++) {
        if (this->allBooks[i].getBookName() == bookName) {
            out << this->allBooks[i].getBookName() << '\n'
                << this->allBooks[i].getBookId() << '\n'
                << this->allBooks[i].getBookAuthor() << '\n'
                << this->allBooks[i].getYearofPub() << '\n'
                << this->allBooks[i].getPrice() << '\n'
                << this->allBooks[i].getStatus() << '\n';
        }
    }
}

void BookList::findBook(unsigned bookId, ostream &out) {
    for (int i = 0; i < this->allBooks.size(); i++) {
        if (this->allBooks[i].getBookId() == bookId) {
            out << this->allBooks[i].getBookName() << '\n'
                << this->allBooks[i].getBookId() << '\n'
                << this->allBooks[i].getBookAuthor() << '\n'
                << this->allBooks[i].getYearofPub() << '\n'
                << this->allBooks[i].getPrice() << '\n'
                << this->allBooks[i].getStatus() << '\n';
        }
    }
}

void BookList::findBooks(string bookAuthor, ostream &out) {
    for (int i = 0; i < this->allBooks.size(); i++) {
        if (this->allBooks[i].getBookAuthor() == bookAuthor) {
            out << this->allBooks[i].getBookName() << '\n'
                << this->allBooks[i].getBookId() << '\n'
                << this->allBooks[i].getBookAuthor() << '\n'
                << this->allBooks[i].getYearofPub() << '\n'
                << this->allBooks[i].getPrice() << '\n'
                << this->allBooks[i].getStatus() << '\n' << '\n';
        }
    }
}


