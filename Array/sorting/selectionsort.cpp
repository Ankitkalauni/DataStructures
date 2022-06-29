// selection sort
#include <vector>
#include  <stdio.h> 
#include <iostream>
using namespace std;

vector<int> selectionsort(vector<int>& arr, int n)
{
    for (int i=0;i<n-1;i++){
        int minindx = i;

        for (int j=i+1; j < n; j++){
            
            if (arr[j] < arr[minindx]){
                minindx = j;
            }
        }

        swap(arr[minindx], arr[i]);
    }
    return arr;
    
}

int main(){
    
    vector<int> arr = {69,4,8,0,3,1,2};
    int length = arr.size();
    vector<int> gg = selectionsort(arr, length);

    for (int p =0;p<length;p++){
        cout <<gg[p]<<" ";
    }

    return 0;
}