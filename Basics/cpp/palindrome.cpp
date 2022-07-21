#include<iostream>
using namespace std;

// TO CONVERT UPPER CASE TO LOWER CASE
/*
'UPPER CASE CHAR' - 'A' + 'a'
    'B'           - 'A' + 'a'
    ascii(66)     -  ascii(65) + ascii(97)

98 = 'b'
*/

char tolower(char x){
    if (x >= 'a' && x<='z'){
        return x;
    }
    else{
        return (x - 'A' + 'a');
    }
}


int stringlen(char arr[]){
    int i = 0;
    for (;arr[i] !='\0';i++);
    return i;
}


int palindrome(char arr[], int n){
    int s=0;
    int e=n-1;

    while(s <= e){
        if (tolower(arr[s++]) != tolower(arr[e--])){
            return 0;
        }
    }

    return 1;
}

int main() {
    char a[10];
    cin>>a;

    int n  = stringlen(a); 

    cout << palindrome(a, n);
    return 0;
}
