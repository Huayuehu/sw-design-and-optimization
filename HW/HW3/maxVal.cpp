# include <iostream>
# include <stdlib.h>
# include <stdio.h>
# include <time.h>
using namespace std;

int findMax(int* arr, int size) {
	int max = 0;
	for (int i = 0; i < size; i++) {
		if (arr[i] > max) max = arr[i];
	}
	return max;
}

void PrintArr(int* arr, int size) {
	for (int i = 0; i < size; i++) {
		cout<<i<<": "<<arr[i]<<endl;
	}
}

int main() {
	srand((unsigned int)time(NULL));
    int arr[888];

    int size = sizeof(arr) / sizeof(arr[0]);
    for(int i = 0; i < size; i++){
        arr[i] = rand() % 100 + 1;
    }
    PrintArr(arr, size);
    cout<<"Maximum Value: "<<findMax(arr, size)<<endl;
}