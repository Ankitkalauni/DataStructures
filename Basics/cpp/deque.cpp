#include<iostream>
#include<deque>
using namespace std;

void print(deque<int> arr){
    for(int i = 0; i < arr.size();i++){
        cout << arr[i]<<endl;
    }
    }

int main() {
    // deqeue

    deque<int> d;
    cout << "\n\ndeque\n\n";
    d.push_back(3);
    d.push_front(4);
    d.push_back(9);
    d.push_back(10);

    print(d);
    d.pop_back();

    print(d);
    d.pop_front();


    // d.erase( d.begin()+1 ); to erase the deque(from where to where)
    // size bcoms zero but capacity stays the same(while using erase)

    return 0;
}
