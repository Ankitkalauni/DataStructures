#include<iostream>
using namespace std;

void reversestring(char arr[], int n){
    int s = 0;
    int e = n-1;
    while (s < e){
    swap(arr[s++], arr[e--]);
    }
}


int stringlen(char arr[]){
    int i = 0;
    for (;arr[i] !='\0';i++);
    return i;
}

int main() {
    char a[10];
    cin>>a;
    int n = stringlen(a);
    reversestring(a, n);

    for (int i = 0; i < n; i ++){
        cout << a[i];
    }
    return 0;
}
