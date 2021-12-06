class Solution {
public:
    int subtractProductAndSum(int n) {
        int product = 1;
        int sum = 0;
        
        while(true){
            
            if (n == 0){
                break;
            }
            else{
                int remainder = n%10;
                product = product * remainder;
                sum = sum + remainder;
                n = n/10;
            }
        }
        
     return product - sum;   
    }
};
