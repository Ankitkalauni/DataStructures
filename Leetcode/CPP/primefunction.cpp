#include <iostream>
#include <math.h>
using namespace std;

bool IsPrime(int n){
    int counter = 2;
    while(counter < n){
        if (n%counter == 0){
            return 0;
        }
        counter +=1;
    }

    return 1;
}

int main(){

    int n;
    cin>>n;

    // cout << n%2;


    bool ans = IsPrime(n);

    if (ans){
    cout << n<<" is a Prime Number";
}
    else{
        cout << n << " is a Composite Number";
    }
    return 0;
}
