#include<iostream>
#include<vector>
using namespace std;

bool rotatesort(vector<int>& arr){
    int count = 0;
    int n = arr.size();

    for (int i = 1; i < n; i++){
        if (arr[i-1] > arr[i]){
            count +=1;
        }

        if (arr[n-1] > arr[0]){
            count +=1;
        }
    }

    return count <= 1;
}

int main() {
    vector<int> arr = {3,4,5,6,7,1,2};


    cout << "Array is sorted and rotated" << endl << rotatesort(arr)<<endl;
    return 0;
}
