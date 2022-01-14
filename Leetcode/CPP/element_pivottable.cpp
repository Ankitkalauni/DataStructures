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

int findk(vector<int> arr, int indx, int key){
    int size = arr.size();
    int start = 0;
    int end = size -1;
    if (key >= arr[0]){
        start = 0;
        end = indx - 1;
    }
    else{
        start = indx;
        end = size - 1;
    }
    cout<<size<<start<<end<<endl;
    while (start <= end){
        int mid = start + (end - start) / 2;

        if (key == arr[mid]){
            return mid;
        }

        else if (key < arr[mid]){
            end = mid - 1;
        }

        else{
            start = mid +1;
        }
    }

    return -1;
}

int main(){

    vector <int> arrr = {7,9,1,2,3};

    int value = pivot(arrr);
    int val = findk(arrr, value, 3);
    cout << val << endl;

}