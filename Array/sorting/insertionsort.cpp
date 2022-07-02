// bubble sort
#include <vector>
#include  <stdio.h> 
#include <iostream>
using namespace std;

void insertionsort(vector<int>& arr, int n)
{
    for (int i = 1; i<n; i++){
        int j = i-1;
        int temp = arr[i];
        while (j>=0){
            if (arr[j] > temp)
            {
                arr[j+1] = arr[j];

            }
            else{
                break;
            }
            j -=1;
        }
        arr[j+1] = temp;
    }
}
int main(){

    vector<int> arr = {6,9,4,1,5,4};
    int n = 6;
    insertionsort(arr, n);

    for (int i=0; i < n; i++){
        cout<<arr[i]<<endl;
    }
}