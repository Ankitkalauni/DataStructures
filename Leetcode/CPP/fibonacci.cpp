#include <iostream>
#include <math.h>
using namespace std;

int bitcount(int x){
    int count = 0;
    
    while(x>0){
        if ((x&1) == 1){
            count+=1;
        }
        x = x>>1;
    }
    return count;
}

void fibonacci(int a, int b, int n){
    cout<<a<<" ";
    int value = 0;

    for (int i=0; i<n; i++){
        cout<<b<<" ";
        value = a + b;
        a = b;
        b = value;
    }
}

int main(){
    fibonacci(0,1,5);
    return 0;
}
