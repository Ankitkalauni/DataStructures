"""
find the square root of the number using binary search log(n) big-O

question link - https://bit.ly/3Dm4hEE 
"""
from nntplib import NNTP


def sqrt(n):
    # Handle corner case
    if(n == 0 or n == 1):
        return n

    start = 2
    end = n

    mid = 0
    while (start < end):
        mid = start + (end - start) // 2
        
        if (mid <= (n//mid)):
            start = mid + 1

        else:
            end = mid

        
    return int(start -1)

if __name__ == '__main__':
    print(sqrt(16))

