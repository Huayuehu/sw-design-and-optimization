//
// Created by Insane on 2020-02-06.
//
#include "BookListTester.h"
#include "BookList.h"
#include "Book.h"
#include <iostream>
#include <fstream>

using namespace std;

void BookListTester::testFindBook() {
    cout << "- findBook()..." << flush;

    /*
     * First, test find book via book name
     */
    cout << " find book via book name" << flush;
    ofstream fout1("/Users/insane/Desktop/USC/20spring/595/lab/lab3/TDD/EC/output.txt");
    assert(fout1.is_open());

    BookList blist("/Users/insane/Desktop/USC/20spring/595/lab/lab3/TDD/EC/inputList.txt");
    blist.findBook("/Users/insane/Desktop/USC/20spring/595/lab/lab3/TDD/EC/inputList.txt", "To kill a Mocking bird", fout1);
    fout1.close();

    // use readFrom() to see whether findBook() worked
    ifstream fin1("/Users/insane/Desktop/USC/20spring/595/lab/lab3/TDD/EC/output.txt");
    assert(fin1.is_open());
    Book Book1;
    Book1.readFrom(fin1);
    assert(Book1.getBookName() == "To kill a Mocking bird");
    assert(Book1.getBookId() == 400148);
    assert(Book1.getBookAuthor() == "Harper Lee");
    assert(Book1.getYearofPub() == "07/16/1960");
    assert(Book1.getPrice() == "$8");
    assert(Book1.getStatus() == "Available");
    fin1.close();
    cout << " passed!   ";


    /*
     * Second, test find book via book ID
     */
    cout << "find book via book ID" << flush;
    ofstream fout2("/Users/insane/Desktop/USC/20spring/595/lab/lab3/TDD/EC/output.txt");
    assert(fout2.is_open());
    blist.findBook("/Users/insane/Desktop/USC/20spring/595/lab/lab3/TDD/EC/inputList.txt", 400148, fout2);
    fout2.close();

    // use readFrom() to see whether findBook() worked
    ifstream fin2("/Users/insane/Desktop/USC/20spring/595/lab/lab3/TDD/EC/output.txt");
    assert(fin2.is_open());
    Book Book2;
    Book2.readFrom(fin2);
    assert(Book2.getBookName() == "To kill a Mocking bird");
    assert(Book2.getBookId() == 400148);
    assert(Book2.getBookAuthor() == "Harper Lee");
    assert(Book2.getYearofPub() == "07/16/1960");
    assert(Book2.getPrice() == "$8");
    assert(Book2.getStatus() == "Available");
    fin2.close();
    cout << " passed! "<< endl;


    /*
     * Third, find all the books via author
     */
//    cout << "find all books written by the author" << flush;


    cout<< "All tests passed! " << endl;
}