#include <iostream>
#include <vector>
using namespace std;

 // program to shift zero to the right.

void rotateK(vector<int> & arr, int k){

    int n = arr.size();
    vector<int> temp(n);

    
    for (int i = 0; i < n; i++){
        temp[(i+k) % n] = arr[i];
        }
    

    for (int i = 0; i < arr.size(); i++){
        arr[i] = temp[i];
    }
}    


int main()
{   
    vector<int> arr = {2,3,0,6,0,5,8};
    
    rotateK(arr, 2);
    
    for (int i = 0; i < 7; i++){
        cout<<arr[i]<<endl;
    }
    return 0;
}
