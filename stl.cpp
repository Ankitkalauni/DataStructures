#include<array>
#include<iostream>
#include<vector>
#include<deque>
#include<list>
#include<queue>
#include<stack>



using namespace std;

void print(deque<int> arr){
    for(int i = 0; i < arr.size();i++){
        cout << arr[i]<<endl;
    }
    }


int main(){

    // vector and array
    int arr[] = {1,2,3,4};
    
    array<int, 4> a = {1,2,3,4};

    vector<int> v;

    vector<int> newvec(5,1); //size of 5 with default value as 1 (else all values are 0)

    vector<int> copyvec(newvec); // copied vector of 'newvec'
    
    v.push_back(1);

    v = {2,5,53};

    cout << v.size(); // tells about the elements alive in a vector

    cout << v.capacity(); // tells about the memory block size

    cout << v.front(); // first element of vector

    cout << v.back(); // last element of vector

    //

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

    // list

    // doublely link-list

    // have to travers through the list to find the element or value
    list<int> lis;

    lis.push_back(3);
    lis.push_front(2);
    
    // stack
    stack<string> s;
    
    s.push("ankit");
    s.push("devraj");
    s.push("kalauni");
    
    cout<< "Element -" << s.top()<< endl; 
    s.pop();
    
    cout << "Top Element -" << s.top() << endl;
    
    cout << "size of stack" << s.size() << endl;
    
    cout << "Empty or not " << s.empty() << endl; 

    
    
    // queue
    queue<string> q; 
    q.push("ankit");
    q.push("devraj");
    q.push("kalauni");


    cout << "Size before pop" << q.size() << endl;
    
    cout << "First element" << q.front() << endl; 
    q.pop();
    
    cout << "First element" << q.front() << endl;
    
    cout << "Size after pop" << q.size() << endl; 

    
    // priority queue

     //max heap
    priority_queue<int> maxi; 
    //min - heap
    priority_queue<int,vector<int> , greater<int> > mini;
    maxi.push(1);
    maxi.push(3);
    maxi.push(2);
    maxi.push(0);
    
    cout<< "size->" <<maxi.size()<<endl;
    int n = maxi.size();
    for(int i = 0;i<n;i++)
    {
        cout<<maxi.top()<<"";
        maxi.pop();
        }
        cout<<endl;

    
    mini.push(1);
    mini.push(0);
    mini.push(4);
    mini.push(3);
    
    int m = mini.size();
    for(int i = 0;i<n;i++)
        {
            cout<<mini.top()<<"";
            mini.pop();
            }
            cout<<endl; 
    /*
    set
    map

    remaining
        */

}
