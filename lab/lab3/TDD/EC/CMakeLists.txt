cmake_minimum_required(VERSION 3.12)
project(EC)

set(CMAKE_CXX_STANDARD 14)

add_executable(EC main.cpp BookTester.h BookTester.cpp Book.h Book.cpp BookList.h BookList.cpp BookListTester.h BookListTester.cpp)