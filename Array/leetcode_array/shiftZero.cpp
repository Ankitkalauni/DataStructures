#include <iostream>
using namespace std;

 // program to shift zero to the right.

void shiftZero(int arr[], int n){

    int i = 0;
    while (i < n-1){
        int temp = i+1;
        while (temp < n){
            if ((arr[i] ==0) and (arr[temp] != 0)){
                swap(arr[i], arr[temp]);
            }

            else if((arr[i] ==0) and (arr[temp] == 0)){
                temp +=1;
            }

            else{
                break;
            }
            
            
        }
        i +=1;
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
