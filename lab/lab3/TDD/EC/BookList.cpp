//
// Created by Huayue Hua on 2020-02-06.
//

#include "BookList.h"
#include <fstream>
#include <vector>

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
    for (auto &allBook : this->allBooks) {
        if (allBook.getBookName() == bookName) {
            out << allBook.getBookName() << '\n'
                << allBook.getBookId() << '\n'
                << allBook.getBookAuthor() << '\n'
                << allBook.getYearofPub() << '\n'
                << allBook.getPrice() << '\n'
                << allBook.getStatus() << '\n';
        }
    }
}

void BookList::findBook(unsigned bookId, ostream &out) {
    for (auto &allBook : this->allBooks) {
        if (allBook.getBookId() == bookId) {
            out << allBook.getBookName() << '\n'
                << allBook.getBookId() << '\n'
                << allBook.getBookAuthor() << '\n'
                << allBook.getYearofPub() << '\n'
                << allBook.getPrice() << '\n'
                << allBook.getStatus() << '\n';
        }
    }
}

void BookList::findBooks(string bookAuthor, ostream &out) {
    for (auto &allBook : this->allBooks) {
        if (allBook.getBookAuthor() == bookAuthor) {
            out << allBook.getBookName() << '\n'
                << allBook.getBookId() << '\n'
                << allBook.getBookAuthor() << '\n'
                << allBook.getYearofPub() << '\n'
                << allBook.getPrice() << '\n'
                << allBook.getStatus() << '\n' << '\n';
        }
    }
}

