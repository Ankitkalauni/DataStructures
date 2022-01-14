#include <iostream>
// #include <math.h>
using namespace std;


void reverse(int arr[], int n){
    // init pointers
    int start = 0;
    int end = n-1;

    while(start <= end){
        // swap values

        swap(arr[start], arr[end]);

        // increment
        start ++;
        end --;

    }
}

void printarr(int arr[], int n){
    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }
}


int main(){

    int a[10] = {1,12,3,4,5,6,7,8,9,0};

    int size = sizeof(a) / sizeof(a[0]);

    reverse(a,size);

    printarr(a, size);

    return 0;
}