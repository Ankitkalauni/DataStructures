// bubble sort
#include <vector>
#include  <stdio.h> 
#include <iostream>
using namespace std;

void bubbleSort(vector<int>& arr, int n)
{   
    int count = 1;
    while (count < n){
        for (int i =  0; i < (n-count); i++){
            if (arr[i] > arr[i+1]){
                swap(arr[i], arr[i+1]);
            }
            
        }
        count +=1;
    }
}

int main(){

    vector<int> arr = {6,9,4,1,5,4};
    int n = 6;
    bubbleSort(arr, n);

    for (int i=0; i < n; i++){
        cout<<arr[i]<<endl;
    }
}