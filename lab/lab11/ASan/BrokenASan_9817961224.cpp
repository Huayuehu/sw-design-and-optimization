#include<stdio.h> 
  
int partition (int arr[], int low, int high) 
{ 
    int pivot = arr[high];    // pivot 
    int i = (low - 1);  // Index of smaller element 
    int temp = 0;
  
    for (int j = low; j <= high-1; j++) 
    { 
        if (arr[j] <= pivot) 
        { 
            i++;    
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        } 
    } 
    //swap(&arr[i + 1], &arr[high]);
    temp = arr[i+1];
    arr[i+1]  = arr[high];
    arr[high] = temp;  
    return (i + 1); 
} 

void quickSort(int arr[], int low, int high) 
{ 
    if (low < high) 
    { 
        int pi = partition(arr, low, high); 
        quickSort(arr, low, pi - 1); 
        quickSort(arr, pi + 1, high); 
    } 
} 
  
/* Function to print an array */
void printArray(int arr[], int size) 
{ 
    int i; 
    for (i=0; i <= size - 1; i++) 
        printf("%d ", arr[i]); 
    printf("n"); 
} 
  
// Driver program to test above functions 
int main() 
{ 
    int arr[] = {10, 7, 8, 9, 1, 5}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
    quickSort(arr, 0, n-1); 
    printf("Sorted array: n"); 
    printArray(arr, n); 
    return 0; 
}