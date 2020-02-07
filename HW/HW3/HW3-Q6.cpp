# include <iostream>
using namespace std;

bool sameside(int x1, int y1, int x2, int y2, double a, double b, double c) {
	double res1 = a * x1 + b * y1 - c;
	double res2 = a * x2 + b * y2 - c;

	if (res1 * res2 > 0) return 1;
	else return 0;
}

int main() {
	//double a = 1, b = 2, c = 3;
	cout<<"Please enter three parameter of line ax+by-c=0 (e.g: 1 2 3): ";
	double a, b, c;
	cin>>a;
	cin>>b;
	cin>>c;
	cout<<"Please enter the first integer points (e.g: 3 4): ";
	int x1;
	int y1;
	cin>>x1;
	cin>>y1;
	cout<<"Please enter the second integer points (e.g: 3 4): ";
	int x2;
	int y2;
	cin>>x2;
	cin>>y2;

	bool res = sameside(x1, y1, x2, y2, a, b, c);
	if (res == 1) cout<<"("<<x1<<", "<<y1<<") and ("<<x2<<", "<<y2<<") lie on the same side of the given line."<<endl;
	else cout<<"("<<x1<<", "<<y1<<") and ("<<x2<<", "<<y2<<") lie on the different side of the given line."<<endl;
}