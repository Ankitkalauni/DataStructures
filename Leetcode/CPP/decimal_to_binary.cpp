#include <iostream>
#include <math.h>
using namespace std;

int main() {

  int n;

  cin>>n;

  int store = 0;
  int i = 0;
  int bit = 0; 
  while(n!=0){

      bit = n&1;
      store = bit * pow(10,i) + store;
      i++;
      n = n>>1; 


  }

  cout<<store;

    }


