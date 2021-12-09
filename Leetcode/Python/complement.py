class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        def decimal_to_binary(n):
            store = 0
            i = 0
            while n != 0:

                bit = n&1
                store += bit * 10 ** i
                n = n >> 1
                i += 1

            return store


        def binary_to_decimal(n):
            ans = 0
            i = 0
            while(n!=0):

                digit = n%10

                if digit:
                    ans += 2 ** i
                
                n = n//10

                i+=1
            return ans

        get_binary = decimal_to_binary(n)
        print(f'binary form of {n} is: ', get_binary)
        rev = ''
        while(get_binary!=0):
            bit = get_binary%10
            print('bit ',bit, end=' ')
            if bit == 1:
                rev += '0'
                print('_0_\n')
            else:
                rev += '1'
                print('_1_\n')
            
            get_binary = get_binary//10

        print(f'reverse binary form of {get_binary} is: ', int(rev))
        get_decimal = binary_to_decimal(int(rev))
        
        return get_decimal

if __name__ == '__main__':

    Solution().bitwiseComplement(10)