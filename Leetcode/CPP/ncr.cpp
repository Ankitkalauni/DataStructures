#include <iostream>
#include <math.h>
using namespace std;

int fact(int n){
    int factor = 1;
    for(int i = 1; i <= n; i++){
        factor *=i;
    }

    return factor;
}

int ncr(int n, int r){
    int num = fact(n);
    int denom = fact(r) * fact(n-r);

    int ans = num / denom;

    return ans;
}

int main() {
    int n,r;
    cin>>n>>r;

    int answer = ncr(n,r);

    cout << answer;
    return 0;

    }


