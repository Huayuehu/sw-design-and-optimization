//
// Created by Huayue Hua on 2020-02-06.
//

#ifndef EC_BOOKLIST_H
#define EC_BOOKLIST_H

#include "Book.h"
#include <vector>

class BookList {
private:
    vector<Book> allBooks;
public:
    explicit BookList(const string& fileName);

    void findBook(string bookName, ostream &out);

    void findBook(unsigned bookId, ostream &out);

    void findBooks(string bookAuthor, ostream& out);
};

#endif //EC_BOOKLIST_H
