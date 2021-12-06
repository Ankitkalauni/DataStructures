def binary_to_decimal(n):
    n = 10101

    ans = 0
    i = 0
    while(n!=0):

        digit = n%10

        if digit:
            ans += 2 ** i
        
        n = n//10

        i+=1
    return ans