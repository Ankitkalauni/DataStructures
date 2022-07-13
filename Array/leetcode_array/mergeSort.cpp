#include <iostream>
using namespace std;

 // program to merge 2 sorted array


void mergeSort(int arr1[],int m,int arr2[],int n,int arr3[]){

    int count = 0;
    int i = 0;
    int j = 0;
    
    while ((i < m) && (j < n)){
            if (arr1[i] < arr2[j]){
                arr3[count++] = arr1[i++];
            }

            else{
                arr3[count++] = arr2[j++];
                
            }    
    }

    while (i < m){
                arr3[count++] = arr1[i++];
    }

    while (j < n){
                arr3[count++] = arr2[j++];
    }
    
}

int main()
{    
    int m=5,n=4;
    
    int arr1[5] = {1,3,5,7,8};
    int arr2[4] = {2,4,6,9};

    int arr3[m+n];

    mergeSort(arr1, m, arr2, n, arr3);


    for (int i =0; i < (m+n); i++){
        cout<<arr3[i]<<endl;
    }
    return 0;

    
    }