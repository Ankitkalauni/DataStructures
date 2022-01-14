#include <iostream>
#include <math.h>
using namespace std;


bool linear(int arr[], int n, int key){
    for (int i =0; i<n; i++){
        if (arr[i] == key){
            return 1;
        }
    }

    return 0;
}

int main(){

    int a[10] = {1,12,3,4,5,6,7,8,9,0};

    int size = sizeof(a) / sizeof(a[0]);
    // int max = GetMax(a, size);

    int key;
    cin>>key;

    bool value = linear(a,size, key);
    
    if (value){
        cout<<"Key is present in the array"<<endl;
    }

    else{
        cout<<"Key is not present in the array"<<endl;
    }

    return 0;
}