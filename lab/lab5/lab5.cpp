#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

struct Profit {
    long double dollar;
    int duration;
};

class KWP {
private:
    Profit p;
    long double weekdata[53];
    long double numsoption[53];
    ofstream file;
public:
    KWP(double b1, double b2, double b3, int duration) {
        file.open("/Users/insane/Desktop/USC/20spring/595/lab/lab5/output.txt",ios::app);

        // initialize part of the weekdata
        weekdata[0] = b1;
        weekdata[1] = 2 * b1 + b2;
        weekdata[2] = 3 * b1 + 2 * (b1 + b2) + b3;
        if (duration > 3) {
            for (int i = 3; i <= duration; i++) {
                weekdata[i] = (b1 + weekdata[i - 1]) + (b2 + weekdata[i - 2]) + (b3 + weekdata[i - 3]);
            }
        }

        // initialize part of numsoption
        numsoption[0] = 1;
        numsoption[1] = 2;
        numsoption[2] = 4;
        if (duration > 3) {
            for (int i = 3; i <= duration; i++) {
                numsoption[i] = numsoption[i - 1] + numsoption[i - 2] + numsoption[i - 3];
            }
        }

        file << "- This is explicit-value constructor for KWP" << endl;
    }

    ~KWP() {
        file << "- This is destructor for KWP" << endl;
        file.close();
    }

    void SetProfit(int duration) {
        // compute sum
        long double pn = weekdata[duration-1];
        // find the total number of option
        long double cn = numsoption[duration-1];
        // set profit
        p.dollar = pn / cn;
        p.duration = duration;
    }

    Profit GetProfit() {
        return  p;
    }

//    /*
//     * Return total numbers of option
//     */
//    int NumsOption(int duration) {
//        if (duration == 1) return 1;
//        if (duration == 2) return 2;
//        if (duration == 3) return 4;
//        return NumsOption(duration - 1) + NumsOption(duration - 2) + NumsOption(duration - 3);
//    }

};


class KYP {
private:
    Profit p;
    ofstream file;
public:
    KYP(int duration) {
        file.open("/Users/insane/Desktop/USC/20spring/595/lab/lab5/output.txt",ios::app);
        p.duration = duration;
        file << "- This is explicit-value constructor for KYP" << endl;
    }

    ~KYP() {
        file << "- This is destructor for KYP" << endl;
        file.close();
    }

    void SetProfit(long double dollar, int U) {
        p.dollar = dollar * U / 100;
    }

    Profit GetProfit() {
        return  p;
    }
};

int main() {
    cout << "Please enter the number of weeks, the number should in between 1 and 52: ";
    int Z;
    cin>>Z;

    ifstream fin("/Users/insane/Desktop/USC/20spring/595/lab/lab5/input.txt");
    ofstream fout("/Users/insane/Desktop/USC/20spring/595/lab/lab5/output.txt");

    /*
     * Read parameters from input.txt
     */
    string b1Str, b2Str, b3Str, UStr, out;
    double b1, b2, b3;
    int U;
    getline(fin, b1Str);
    getline(fin, b1Str);
    getline(fin, b2Str);
    getline(fin, b3Str);
    getline(fin, UStr);
    getline(fin, UStr);
    istringstream is1(b1Str);
    is1>>out;
    is1>>out;
    b1 = stod(out);
    istringstream is2(b2Str);
    is2>>out;
    is2>>out;
    b2 = stod(out);
    istringstream is3(b3Str);
    is3>>out;
    is3>>out;
    b3 = stod(out);
    U = stoi(UStr);

    /*
     * Calculate profit for Kanye West
     */
    KWP kwp(b1, b2, b3, Z);
    kwp.SetProfit(Z);
    Profit res1 = kwp.GetProfit();

    /*
     * Calculate profit for Kourosh Yaghmaei
     */
    KYP kyp(res1.duration);
    kyp.SetProfit(res1.dollar, U);
    Profit res2 = kyp.GetProfit();

    // display result and close the files
    cout << "KW's profit for " << res1.duration << " number of weeks in average is estimated $" << res1.dollar << ", out of which " << U << "%, i.e., $" << res2.dollar << " is KY's." << endl;
    fin.close();
    fout.close();

    return 0;
}