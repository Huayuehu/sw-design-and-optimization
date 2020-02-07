//
// Created by Insane on 2020-02-06.
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

void BookList::findBook(const string &fileName, string bookName, ostream &out) {
    BookList list(fileName);
    for (auto &allBook : list.allBooks) {
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

void BookList::findBook(const string &fileName, unsigned bookId, ostream &out) {
    BookList list(fileName);
    for (int i = 0; i < list.allBooks.size(); i++) {
        if (list.allBooks[i].getBookId() == bookId) {
            out << list.allBooks[i].getBookName() << '\n'
                << list.allBooks[i].getBookId() << '\n'
                << list.allBooks[i].getBookAuthor() << '\n'
                << list.allBooks[i].getYearofPub() << '\n'
                << list.allBooks[i].getPrice() << '\n'
                << list.allBooks[i].getStatus() << '\n';
        }
    }
}

void BookList::findBooks(string bookAuthor, ostream &out) {

}
