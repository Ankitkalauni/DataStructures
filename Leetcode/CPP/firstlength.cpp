#include <iostream>
#include <math.h>
#include <vector>

using namespace std;


int findleftkey(vector<int>& arr, int size, int key){
    int start = 0;
    int end = size -1;

    int ans = -1;

    while(start <= end){
        int mid = start + (end - start) / 2; //find the mid

        if (key == arr[mid]){
            ans = mid;
            end = mid -1;

        }

        if (key < arr[mid]){
            end = mid - 1;
        }

        else if (key > arr[mid]){
            start = mid + 1;
        }
    }


    return ans;
}

int findrightkey(vector<int>& arr, int size, int key){
    int start = 0;
    int end = size -1;

    int ans = -1;

    while(start <= end){
        int mid = start + (end - start) /2; //find the mid

        if (key == arr[mid]){
            ans = mid;
            start = mid + 1;

        }

        if (key > arr[mid]){
            start = mid + 1;
        }

        else if (key < arr[mid]){
            end = mid - 1;
        }
    }


    return ans;
}  
pair<int, int> firstAndLastPosition(vector<int>& arr, int n, int k)
{
    pair<int, int> p;
    
    p.second = findrightkey(arr, n, k);
    p.first = findleftkey(arr, n, k);

    return p;

}