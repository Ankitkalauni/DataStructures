#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

//find the peek index of the moutain array in cpp
int peek(vector<int> arr){
    int start = 0; 
    int end = arr.size() - 1;
    int mid = start + (end - start) / 2;
    while(start < end){

        if (arr[mid] < arr[mid + 1]){
            start = mid + 1;
        }

        else{
            end = mid;
        }

        mid = start + (end - start) / 2;
    }

    return mid;
}

int main(){

    vector <int> arrr = {3,4,5,1};

    int value = peek(arrr);

    cout << value << endl;

}