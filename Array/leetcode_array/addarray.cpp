#include<iostream>
#include<vector>
using namespace std;

void addarray(vector<int>& arr1, vector<int>& arr2, vector<int>& arr3){

    int n = arr1.size(); //size of arr1
    int m = arr2.size(); //size of arr2

    int i = n - 1; //last index of arr1
    int j = m - 1; //last index of arr2

    int carry = 0;
    int sum = 0;
    int ans;

    while ((i >= 0) && (j >= 0)){
        int sum = arr1[i] + arr2[j] + carry;
        
        carry = sum / 10;
        ans = sum%10;

        arr3.insert(arr3.begin(),ans);

        i-=1;
        j-=1;
    }

    while (i >= 0){
            sum = arr1[i] + carry;
            carry = sum / 10;
            ans = sum % 10;
            arr3.insert(arr3.begin(),ans);
            i-=1;

    }

    while (j >= 0){
            sum = arr2[j] + carry;
            carry = sum / 10;
            ans = sum % 10;
            arr3.insert(arr3.begin(),ans);
            j-=1;

    }
    
    while( carry !=0){
        sum = carry;
        carry = sum / 10;
        ans = sum % 10;
        arr3.insert(arr3.begin(),ans);
    }

}

int main() {
    vector<int> arr1 = {9,9,9,9};
    vector<int> arr2 = {9,9,9,9};
    vector<int> arr3;
    
    addarray(arr1,arr2,arr3);

    
    cout <<endl;
    for (int i=0; i< arr3.size(); i ++){
        cout << arr3[i];
    }
    return 0;
}
