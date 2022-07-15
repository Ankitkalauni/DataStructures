#include<iostream>
#include<set>
using namespace std;



int main() {
    // set<int> s1; // defining an empty set
    set<int> s1 = {6, 10, 5, 1}; // defining a set with values

    // insert elements in random order 
    s1.insert(40); 
    s1.insert(30); 
    s1.insert(60); 
    s1.insert(20); 
    s1.insert(50); 
  
    // only one 50 will be added to the set 
    s1.insert(50); 
    s1.insert(10);


    set<int>::iterator itr;
   
  // Displaying set elements
  for (itr = s1.begin();
       itr != s1.end(); itr++)
  {
    cout << *itr << " ";
  }

    return 0;
}
