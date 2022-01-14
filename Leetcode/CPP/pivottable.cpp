#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

int pivot(vector<int> arr){
    int size = arr.size();
    int start = 0;
    int end = size - 1;

    while (start < end){
        int mid = start + (end - start) /2;

        if (arr[mid] >= arr[0]){
            start = mid + 1;
        }

        else{
            end = mid;
        }
    }

    return start;

}

int main(){

    vector <int> arrr = {7,9,1,2,3};

    int value = pivot(arrr);

    cout << value << endl;

}