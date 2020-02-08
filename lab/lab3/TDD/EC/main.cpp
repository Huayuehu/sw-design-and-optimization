// This is main.cpp for Book part

#include <iostream>
#include "BookTester.h"
#include "BookListTester.h"

using namespace std;

int main() {
    BookTester bookTester;
    bookTester.runTests();

    BookListTester bookListTester;
    bookListTester.testFindBook();
}