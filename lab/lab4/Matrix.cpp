#include <iostream>
#include <fstream>
#include <cassert>

using namespace std;

class Matrix {
public:
    int value[20][10];
    int repeat_row_index;
    int linear_search(int num, ostream &out);
    void sort_row(ostream &out);
    void binary_search(int num, ostream &out);
};

int Matrix::linear_search(int num, ostream &out) {
    int count = 0;
    for (int k = 1 ; k < 10; k++) {
        if (value[0][k] == num) {
            out << "Iteration number of linear search for FirstNum: " << count << endl;
            repeat_row_index = 0;
            return 0;
        }
        count++;
    }
    for (int i = 1; i < 20; i++) {
        for (int j = 0; j < 10; j++) {
            if (value[i][j] == num) {
                out << "Linear search iteration times: " << count << endl;
                repeat_row_index = i;
                return i;
            }
            count++;
        }
    }
    return -1;
}

void Matrix::sort_row(ostream &out) {
    int n =  9;
    while (n >= 1) {
        for (int i = 0; i < n; i++) {
            if (value[repeat_row_index][i] >= value[repeat_row_index][i + 1]) {
                int temp = value[repeat_row_index][i + 1];
                value[repeat_row_index][i + 1] = value[repeat_row_index][i];
                value[repeat_row_index][i] = temp;
            }
        }
        n--;
    }
    out << "The sorted row including FirstNum: ";
    for (int i = 0; i < 9; i++) {
        out << value[repeat_row_index][i] << ", ";
    }
    out << value[repeat_row_index][9] << endl;
}

void Matrix::binary_search(int num, ostream &out) {
    int count = 1;
    int start = 0, end = 9;
    while (start <= end) {
        int mid = start + (end - start) / 2;
        if (value[repeat_row_index][mid] == num) {
            out << "The index of FirstNum obtained from the binary search: " << mid << endl;
            out << "The iteration time of using the binary search: " << count << endl;
            return;
        }
        else if (value[repeat_row_index][mid] < num) {
            start = mid + 1;
            count++;
        }
        else {
            end = mid - 1;
            count++;
        }
    }
    return;
}



int main() {
    ifstream fin("./input.txt");
    ofstream fout("./output.txt");
    assert(fin.is_open());
    assert(fout.is_open());

    fout << "/********************************/" << endl << endl;

    Matrix matrix;
    for (int i = 0; i < 20; i++) {
        for (int j = 0; j < 10; j++) {
            fin >> matrix.value[i][j];
        }
    }
    int FirstNum = matrix.value[0][0];
    matrix.linear_search(FirstNum, fout);
    matrix.sort_row(fout);
    matrix.binary_search(FirstNum, fout);

    fout << endl;
    fout << "/********************************/" << endl;

    fin.close();
    fout.close();
    return 0;
}