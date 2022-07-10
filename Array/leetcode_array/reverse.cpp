#include <iostream>
using namespace std;


void swap_arr(int arr[], int n)
{
    int start = 0;
    int end = n-1;

    while (start < end){
        swap(arr[start], arr[end]);

        start +=1;
        end -=1;
    }
}


int main()
{    
    int arr[] = {11,22,33,44};
    int n = sizeof(arr) / sizeof(arr[0]);
    swap_arr(arr,n);
    
    for (int i=0; i < n; i++){
        cout<< arr[i]<<endl;
    }
    
}