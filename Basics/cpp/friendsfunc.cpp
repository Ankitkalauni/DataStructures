#include <iostream>
#include <vector>
using namespace std;

 // friend function and classes.
class sum;
class product;

class product{
    public:
    void print(sum s1);
    product(sum s1);
};

class sum{
    int c;
    int _a,_b;
    
    // friend void product :: print(sum s1);
    friend class product;

    public:
        void print(){
            cout << c;
        }
        sum(int a, int b){
            _a  = a;
            _b = b;
            c = _a + _b;
            sum :: print();
        }
};


void product :: print(sum s1){
        cout <<endl<< "a+b = "<< (s1._a * s1._b)<<endl;
    }

product :: product(sum s1){

        product :: print(s1);
    }


int main()
{   

    sum a1(3,2);

    product prod(a1);
    
    return 0;
}
