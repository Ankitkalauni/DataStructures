#include<iostream>
#include<map>
using namespace std;


    /*
    Maps are associative containers that store
    elements in a mapped fashion. Each element
    has a key value and a mapped value. No two
    mapped values can have the same key values.


    */

int main() {

    // empty map container
    map<int, int> map_temp;
  
    // insert elements in random order
    map_temp.insert(pair<int, int>(1, 40));
    map_temp.insert(pair<int, int>(2, 30));
    map_temp.insert(pair<int, int>(3, 60));
    map_temp.insert(pair<int, int>(4, 20));
    map_temp.insert(pair<int, int>(5, 50));
    map_temp.insert(pair<int, int>(6, 50));
      
      map_temp[7]=10;     // another way of inserting a value in a map
     
  
    // printing map map_temp
    map<int, int>::iterator itr;
    cout << "\nThe map map_temp is : \n";
    cout << "\tKEY\tELEMENT\n";
    for (itr = map_temp.begin(); itr != map_temp.end(); ++itr) {
        cout << '\t' << itr->first << '\t' << itr->second
             << '\n';
    }
    cout << endl;

    return 0;
}
