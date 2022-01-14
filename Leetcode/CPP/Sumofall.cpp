#include <iostream>
#include <math.h>
using namespace std;


int sumofall(int arr[], int n){
    int count = 0;

    for (int i=0; i<n; i++){
        count += arr[i];
    }

    return count;
}

int main(){

    int a[10] = {1,12,3,4,5,6,7,8,9,0};

    int size = sizeof(a) / sizeof(a[0]);
    // int max = GetMax(a, size);
    int count = sumofall(a,size);
    cout << count;
    return 0;
}