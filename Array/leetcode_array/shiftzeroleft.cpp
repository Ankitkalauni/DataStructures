#include <iostream>
using namespace std;

 // program to shift zero to the right.

void shiftZero(int arr[], int n){

    int i = 0;

    for (int j = 0; j < n; j++){
        if (arr[j] == 0){
            swap(arr[j], arr[i]);
            i +=1;
        }
    }
    }

int main()
{   
    int arr[7] = {2,3,0,6,0,5,8};
    
    shiftZero(arr, 7);
    
    for (int i = 0; i < 7; i++){
        cout<<arr[i]<<endl;
    }
    return 0;

    
    }

