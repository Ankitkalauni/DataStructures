#include <iostream>
#include <math.h>
using namespace std;

int GetMax(int arr[], int n){
    int max = INT32_MIN;

    for (int i=0; i<n; i++){
        if(arr[i] > max){
            max = arr[i];
        }
    }

    return max;
}

int main(){

    int a[10] = {1,12,3,4,5,6,7,8,9,0};
    int size = sizeof(a) / sizeof(a[0]);
    int max = GetMax(a, size);

    cout << max;
    return 0;
}