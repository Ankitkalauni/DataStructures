#include<iostream>
#include<vector>
#include<array>
using namespace std;

int main() {
    // vector and array
    int arr[] = {1,2,3,4};
    
    array<int, 4> a = {1,2,3,4};

    vector<int> v;

    vector<int> newvec(5,1); //size of 5 with default value as 1 (else all values are 0)

    vector<int> copyvec(newvec); // copied vector of 'newvec'
    
    v.push_back(1);

    v = {2,5,53};

    cout << v.size(); // tells about the elements alive in a vector

    cout << v.capacity(); // tells about the memory block size

    cout << v.front(); // first element of vector

    cout << v.back(); // last element of vector

    return 0;
}
