#include<iostream>
#include<stack>
using namespace std;



int main() {
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

    return 0;
}
