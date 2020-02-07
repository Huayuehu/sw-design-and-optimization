//
// Created by Huayue Hua on 2020-02-06.
//
#include "BookTester.h"
#include "Book.h"
#include <iostream>
#include <fstream>

using namespace std;

void BookTester::runTests() {
    cout << "Test class Book..." << endl;
    testConstructor();
    testReadFrom();
    cout << "All tests passed!" << endl << endl;
}

void BookTester::testConstructor() {
    cout << "- constructor..." << flush;

    // expilict-value constructor
    Book Book1("To kill a Mocking bird", 400148, "Harper Lee", "07/16/1960", "$8", "Available");
    assert(Book1.getBookName() == "To kill a Mocking bird");
    assert(Book1.getBookId() == 400148);
    assert(Book1.getBookAuthor() == "Harper Lee");
    assert(Book1.getYearofPub() == "07/16/1960");
    assert(Book1.getPrice() == "$8");
    assert(Book1.getStatus() == "Available");
    cout << " 0 " << flush;

    Book Book2("The Book Thief", 400149, "Markus Zusak", "07/11/2005", "$10", "Available");
    assert(Book2.getBookName() == "The Book Thief");
    assert(Book2.getBookId() == 400149);
    assert(Book2.getBookAuthor() == "Markus Zusak");
    assert(Book2.getYearofPub() == "07/11/2005");
    assert(Book2.getPrice() == "$10");
    assert(Book2.getStatus() == "Available");
    cout << " 1 " << flush;

    Book Book3("The Great Gatsby", 400150, "F. Scott Fitzgerald", "05/15/1980", "$9", "Unvailable");
    assert(Book3.getBookName() == "The Great Gatsby");
    assert(Book3.getBookId() == 400150);
    assert(Book3.getBookAuthor() == "F. Scott Fitzgerald");
    assert(Book3.getYearofPub() == "05/15/1980");
    assert(Book3.getPrice() == "$9");
    assert(Book3.getStatus() == "Unvailable");
    cout << " 2 " << flush;

    Book Book4("The Kite Runner", 400168, "Khaled Hosseini", "07/23/2000", "$12", "Unvailable");
    assert(Book4.getBookName() == "The Kite Runner");
    assert(Book4.getBookId() == 400168);
    assert(Book4.getBookAuthor() == "Khaled Hosseini");
    assert(Book4.getYearofPub() == "07/23/2000");
    assert(Book4.getPrice() == "$12");
    assert(Book4.getStatus() == "Unvailable");
    cout << " 3 " << flush;

    Book Book5("Lord of the Flies", 400176, "William Golding", "08/18/1980", "$14", "Available");
    assert(Book5.getBookName() == "Lord of the Flies");
    assert(Book5.getBookId() == 400176);
    assert(Book5.getBookAuthor() == "William Golding");
    assert(Book5.getYearofPub() == "08/18/1980");
    assert(Book5.getPrice() == "$14");
    assert(Book5.getStatus() == "Available");
    cout << " 4 " << flush;

    Book Book6("Go Set a Watchman", 400198, "Harper Lee", "07/16/1972", "$8", "Available");
    assert(Book6.getBookName() == "Go Set a Watchman");
    assert(Book6.getBookId() == 400198);
    assert(Book6.getBookAuthor() == "Harper Lee");
    assert(Book6.getYearofPub() == "07/16/1972");
    assert(Book6.getPrice() == "$8");
    assert(Book6.getStatus() == "Available");
    cout << " 5 " << flush;

    cout << " Passed!" << endl;
}

void BookTester::testReadFrom() {
    cout << "- readFrom()..." << flush;

    ifstream fin("/Users/insane/Desktop/USC/20spring/595/lab/lab3/TDD/EC/inputList.txt");
    assert(fin.is_open());
    Book Book1;

    Book1.readFrom(fin);
    assert(Book1.getBookName() == "To kill a Mocking bird");
    assert(Book1.getBookId() == 400148);
    assert(Book1.getBookAuthor() == "Harper Lee");
    assert(Book1.getYearofPub() == "07/16/1960");
    assert(Book1.getPrice() == "$8");
    assert(Book1.getStatus() == "Available");
    cout << " 0 " << flush;

    string seperator;
    getline(fin, seperator);
    Book1.readFrom(fin);
    assert(Book1.getBookName() == "The Book Thief");
    assert(Book1.getBookId() == 400149);
    assert(Book1.getBookAuthor() == "Markus Zusak");
    assert(Book1.getYearofPub() == "07/11/2005");
    assert(Book1.getPrice() == "$10");
    assert(Book1.getStatus() == "Available");
    cout << " 1 " << flush;

    getline(fin, seperator);
    Book1.readFrom(fin);
    assert(Book1.getBookName() == "The Great Gatsby");
    assert(Book1.getBookId() == 400150);
    assert(Book1.getBookAuthor() == "F. Scott Fitzgerald");
    assert(Book1.getYearofPub() == "05/15/1980");
    assert(Book1.getPrice() == "$9");
    assert(Book1.getStatus() == "Unvailable");
    cout << " 2 " << flush;

    getline(fin, seperator);
    Book1.readFrom(fin);
    assert(Book1.getBookName() == "The Kite Runner");
    assert(Book1.getBookId() == 400168);
    assert(Book1.getBookAuthor() == "Khaled Hosseini");
    assert(Book1.getYearofPub() == "07/23/2000");
    assert(Book1.getPrice() == "$12");
    assert(Book1.getStatus() == "Unvailable");
    cout << " 3 " << flush;

    getline(fin, seperator);
    Book1.readFrom(fin);
    assert(Book1.getBookName() == "Lord of the Flies");
    assert(Book1.getBookId() == 400176);
    assert(Book1.getBookAuthor() == "William Golding");
    assert(Book1.getYearofPub() == "08/18/1980");
    assert(Book1.getPrice() == "$14");
    assert(Book1.getStatus() == "Available");
    cout << " 4 " << flush;

    getline(fin, seperator);
    Book1.readFrom(fin);
    assert(Book1.getBookName() == "Go Set a Watchman");
    assert(Book1.getBookId() == 400198);
    assert(Book1.getBookAuthor() == "Harper Lee");
    assert(Book1.getYearofPub() == "07/16/1972");
    assert(Book1.getPrice() == "$8");
    assert(Book1.getStatus() == "Available");
    cout << " 5 " << flush;
    fin.close();

    cout << " Passed!" << endl;
}