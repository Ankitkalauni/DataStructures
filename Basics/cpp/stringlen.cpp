#include<iostream>
using namespace std;

int stringlen(char arr[]){
    int i = 0;
    for (;arr[i] !='\0';i++);
    return i;
}

int main() {
    char a[10];
    cin >>a;

    cout<< stringlen(a);

    return 0;
}
